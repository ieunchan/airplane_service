from rest_framework import generics
from .models import Flight
from .serializers import FlightSerializer
from django.views.generic import ListView

class FlightList(ListView):
    model = Flight

class FlightListCreateAPIView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


