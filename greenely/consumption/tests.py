import time
from datetime import datetime, timedelta
from django.urls import reverse
from rest_framework import status
from rest_framework.test import (APITestCase,
                                 APIRequestFactory)
from .models import days, months


class Consumption_Data_Test(APITestCase):
    def setUp(self):
        self.user_data = {
            "username": "greenelyuser",
            "password": "somepassword",
            "re_password": "somepassword",
            "address": "tehran",
            "mobile_number": "09128122752",
            "first_name": "Mohammad",
            "last_name": "Rezaei",
            "birth_date": "1988-09-20",
            "birth_place": "Tehran",
            "email": "test@yahoo.com"
        }
        self.month_query_params = {
            "resolution": "M",
            "count": 3,
            "start": "2014-09-1"
        }

        self.day_query_params = {
            "resolution": "D",
            "count": 6,
            "start": "2014-03-1"
        }

        self.factory = APIRequestFactory()
        self.sign_up_url = reverse('signup')
        response = self.client.post(self.sign_up_url, self.user_data, format='json')
        self.user_id = response.data["id"]
        self.token = 'JWT ' + response.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.data_url = reverse('data')
        self.limit_url = reverse('limit')

    def test_get_months_data_list(self):
        start = datetime.strptime(self.month_query_params["start"], '%Y-%m-%d')
        response = self.client.get(self.data_url, self.month_query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), months.objects.filter(user_id=self.user_id,
                                                                           timestamp__range=[start, start + timedelta(
                                                                               days=int(self.month_query_params[
                                                                                            "count"]) * 31)]).count())

    def test_get_days_data_list(self):
        start = datetime.strptime(self.day_query_params["start"], '%Y-%m-%d')
        response = self.client.get(self.data_url, self.day_query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']),
                         days.objects.filter(user_id=self.user_id,
                                                timestamp__range=[start,
                                                 start + timedelta(
                                                     days=int(
                                                         self.day_query_params[
                                                             "count"]))]).count())
    def test_get_data_list_without_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(self.data_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_data_list_without_params(self):
        response = self.client.get(self.data_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_data_list_wrong_resolution(self):
        self.month_query_params["resolution"]="T"
        response = self.client.get(self.data_url, self.month_query_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_data_list_wrong_count(self):
        self.month_query_params["count"] = "ABC"
        response = self.client.get(self.data_url, self.month_query_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_data_list_wrong_start(self):
        self.month_query_params["count"] = "2014-AD-13"
        response = self.client.get(self.data_url, self.month_query_params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_limit_list_without_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(self.limit_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_limit_list(self):
        response = self.client.get(self.limit_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
