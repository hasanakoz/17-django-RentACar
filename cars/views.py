from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer

from .models import Car, Reservation
from .permissions import IsStaffOrReadOnly

# Create your views here.


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsStaffOrReadOnly,]
