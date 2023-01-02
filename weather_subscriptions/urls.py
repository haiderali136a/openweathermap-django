from django.urls import path
from weather_subscriptions import views

urlpatterns = [
    path(r'', views.SubscriptionViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='subscription-list'),
    path('<int:pk>/', views.SubscriptionViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                                        'put': 'update'}), name='subscription-detail'),
]