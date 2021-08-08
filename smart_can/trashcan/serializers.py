from rest_framework import serializers
from trashcan.models import Can, Occupancy

class CanList(serializers.ModelSerializer):
    class Meta:
        model = Can
        fields = ['address', 'identifier', 'volume', 'pk']



class CanDetail(serializers.ModelSerializer):
    class Meta:
        model = Can
        fields = ['address', 'identifier', 'volume', 'pk', 'current_percent']


class OccupancyList(serializers.ModelSerializer):
    class Meta:
        model = Occupancy
        fields = ['time', 'percentage']


class CanOccupancyTrace(serializers.ModelSerializer):
    occupancy_set = OccupancyList(many=True)
    class Meta:
        model = Can
        fields = ['occupancy_set']
