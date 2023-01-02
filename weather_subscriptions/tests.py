from django.test import TestCase
from .models import Subscription
from rest_framework.test import APITestCase


# models test

class SubscriptionTest(APITestCase):

    def create_subscription(self, email="abc@gmail.com", location="London"):
        return Subscription.objects.create(email=email, location=location,
                                           weather_conditions="temperature less than 30")

    def test_subscription_model(self):
        w = self.create_subscription()
        self.assertTrue(isinstance(w, Subscription))

    # views

    def test_subscription_create_view(self):
        url = '/subscriptions/'
        data = {'email': 'xyz@gmail.com', 'location': 'Lahore', 'weather_conditions': 'temperature higher than 5'}
        resp = self.client.post(url, data)

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['location'], resp.json()['location'])

    def test_subscription_retrieve_view(self):
        url = '/subscriptions/'
        data = {'email': 'xyz@gmail.com', 'location': 'Lahore', 'weather_conditions': 'temperature higher than 5'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['location'], resp.json()['location'])

        url = f'/subscriptions/{resp.json()["id"]}/'
        resp = self.client.get(url)
        self.assertEqual(data['location'], resp.json()['location'])
        self.assertEqual(resp.status_code, 200)

    def test_subscription_update_view(self):
        url = '/subscriptions/'
        data = {'email': 'xyz@gmail.com', 'location': 'Lahore', 'weather_conditions': 'temperature higher than 5'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['location'], resp.json()['location'])

        url = f'/subscriptions/{resp.json()["id"]}/'
        data = {'email': 'xyz@gmail.com', 'location': 'Lahore', 'weather_conditions': 'temperature higher than 1'}
        resp = self.client.put(url, data)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['weather_conditions'], resp.json()['weather_conditions'])
