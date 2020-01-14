from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import DataViewSet

# router = DefaultRouter()
# router.register(r'', DataViewSet, base_name='flight')

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^data/$', DataViewSet.as_view()),
]
