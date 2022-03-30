from django.db import models


class MapsMarker(models.Model):
    pointer = models.CharField(max_length=200)

    def __str__(self):
        return self.pointer
