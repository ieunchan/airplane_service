from django.urls import path
from .views import FlightListCreateAPIView, FlightRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('flights/', FlightListCreateAPIView.as_view(), name='flight-list-create'),
    path('flights/<int:pk>/', FlightRetrieveUpdateDestroyAPIView.as_view(), name='flight-detail'),
]
