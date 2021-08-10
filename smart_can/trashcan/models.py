from django.db import models

# Create your models here.

class Can(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    volume = models.FloatField()

    def current_occupancy(self):
        return self.occupancy_set.last()

    def current_percent(self):
        return self.current_occupancy().percentage

    def door_counter(self):
        return self.doorusage_set.count()



class Occupancy(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    percentage = models.FloatField(null = False)
    can = models.ForeignKey(Can, on_delete=models.CASCADE)
    class Meta:
        ordering = ['time']


class DoorUsage(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    can = models.ForeignKey(Can, on_delete=models.CASCADE)

