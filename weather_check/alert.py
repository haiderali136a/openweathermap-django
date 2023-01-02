import requests
from openweatherapi.settings import OPENWEATHERMAP_API_KEY, OPENWEATHER_API_URL
from weather_subscriptions.models import Subscription
from weather_subscriptions.utils import compare_weather_conditions


def check_conditions():
    subscriptions = Subscription.objects.filter(is_active=True)
    for subscription in subscriptions:
        # Make a request to the weather API
        url = f'{OPENWEATHER_API_URL}?q={subscription.location}&' \
              f'appid={OPENWEATHERMAP_API_KEY}'
        response = requests.get(url)
        current_data = response.json()
        # Check the temperature against the threshold
        expected_weather_condition = subscription.weather_conditions
        weather_check = compare_weather_conditions(current_data, expected_weather_condition)
        if weather_check:
            subscription.is_active = False
            subscription.save()
            # Log the alert
            with open('alerts.txt', 'a') as f:
                f.write(f'Weather condition: {subscription.weather_conditions} met in location: '
                        f'{subscription.location}\n')


# check_conditions()