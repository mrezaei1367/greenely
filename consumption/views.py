import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from base.pagination import BasePagination
from .models import days, months

error_logger = logging.getLogger('error_logger')


class DataViewSet(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = BasePagination

    def list(self, request, *args, **kwargs):
        pass
