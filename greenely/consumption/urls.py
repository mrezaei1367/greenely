from django.conf.urls import url
from .views import DataView, LimitView
from .default_values import (DATA_API_PATH, LIMIT_API_PATH)

urlpatterns = [
    url(DATA_API_PATH, DataView.as_view()),
    url(LIMIT_API_PATH, LimitView.as_view()),
]
