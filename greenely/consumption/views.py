import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from .utils import (retrieve_data, make_errors_format, serialize_data_output,
                    retrieve_limit)
from .errors import SERVER_ERROR
from .default_values import (RESPONSE, ERROR_LOGGER)

error_logger = logging.getLogger(ERROR_LOGGER)


class DataView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This method use for get the queryset
        :return: 
        """
        errors, queryset = retrieve_data(self.request)
        if len(errors) == 0:
            return [], queryset
        else:
            return errors, False

    def get(self, request):
        """
            resolution -- A parameter with value "M" for month and "D" for day
            start -- A  parameter that show a date like '2014-03-01'
            count -- A parameter that is a number like 5
            This method use for get all of current user data consumption based on the query parameter
        """
        try:
            errors, queryset = self.get_queryset()
            if len(errors) == 0:
                response = serialize_data_output(queryset)
                return Response(response, status.HTTP_200_OK)
            else:
                errs = make_errors_format(errors, request.path)
                return Response(errs, status.HTTP_400_BAD_REQUEST)
        except:
            errs = make_errors_format([SERVER_ERROR], request.path)
            error_logger.error({RESPONSE: errs})
            return Response(errs, status.HTTP_400_BAD_REQUEST)


class LimitView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        This method return the minimum and maximum consumption of current user
        :param request: 
        :return: 
        """
        try:
            response = retrieve_limit(request)
            return Response(response, status.HTTP_200_OK)
        except:
            errs = make_errors_format([SERVER_ERROR], request.path)
            error_logger.error({RESPONSE: errs})
            return Response(errs, status.HTTP_400_BAD_REQUEST)
