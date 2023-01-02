from rest_framework import viewsets
from rest_framework.response import Response
from weather_subscriptions.models import Subscription
from weather_subscriptions.serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
