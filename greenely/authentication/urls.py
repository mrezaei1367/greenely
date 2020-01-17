from django.conf.urls import url
from authentication.views import (
    SignupView,
    LoginByPasswordView,
)
from .default_values import (SIGNUP_API_PATH, LOGIN_API_PATH)

urlpatterns = [
    url(SIGNUP_API_PATH, SignupView.as_view(), name="signup"),
    url(LOGIN_API_PATH, LoginByPasswordView.as_view(), name="login"),
]
