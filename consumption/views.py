import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from base.pagination import BasePagination
from .serializers import DayDataSerializer, MonthDataSerializer
from .utils import retrieve_data, make_errors_format
from .errors import SERVER_ERROR
from .default_values import DAY, MONTH, RESOLUTION

error_logger = logging.getLogger('error_logger')


class DataViewSet(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = BasePagination

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
                page = self.paginate_queryset(queryset)
                if request.GET.get(RESOLUTION) == DAY:
                    serializer = DayDataSerializer(page, many=True)
                elif request.GET.get(RESOLUTION) == MONTH:
                    serializer = MonthDataSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            else:
                errs = make_errors_format(errors, request.path)
                return Response(errs, status.HTTP_400_BAD_REQUEST)
        except:
            errs = make_errors_format([SERVER_ERROR], request.path)
            error_logger.error({'response': errs})
            return Response(errs, status.HTTP_400_BAD_REQUEST)
