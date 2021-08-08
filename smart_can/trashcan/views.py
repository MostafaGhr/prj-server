from django.shortcuts import render
from rest_framework import mixins, generics

from trashcan.models import Can, Occupancy
from . import serializers

# Create your views here.

class CanView(generics.ListAPIView):
    queryset = Can.objects.all()
    serializer_class = serializers.CanList


class CanDetailView(generics.RetrieveAPIView):
    queryset = Can.objects.all()
    serializer_class = serializers.CanDetail
    

class OccupancyView(generics.ListAPIView):
    queryset = Occupancy.objects.all()
    serializer_class = serializers.OccupancyList


class CanHistoryView(generics.RetrieveAPIView):
    queryset = Can.objects.all()
    serializer_class = serializers.CanOccupancyTrace