from django.conf.urls import url
from .views import DataViewSet
from .default_values import (DATA_API_PATH, LIMIT_API_PATH)

urlpatterns = [
    url(DATA_API_PATH, DataViewSet.as_view()),
    url(LIMIT_API_PATH, DataViewSet.as_view()),
]
