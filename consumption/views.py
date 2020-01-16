import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from .utils import (retrieve_data, make_errors_format, serialize_output)
from .errors import SERVER_ERROR

error_logger = logging.getLogger('error_logger')


class DataViewSet(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        errors, queryset = retrieve_data(self.request)
        if len(errors) == 0:
            return [], queryset
        else:
            return errors, False

    def get(self, request):
        try:
            errors, queryset = self.get_queryset()
            if len(errors) == 0:
                response = serialize_output(queryset)
                return Response(response, status.HTTP_200_OK)
            else:
                errs = make_errors_format(errors, request.path)
                return Response(errs, status.HTTP_400_BAD_REQUEST)
        except:
            errs = make_errors_format([SERVER_ERROR], request.path)
            error_logger.error({'response': errs})
            return Response(errs, status.HTTP_400_BAD_REQUEST)
