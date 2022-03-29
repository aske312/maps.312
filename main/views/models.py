from django.db import models
from djgeojson.fields import PolygonField


class MapsMarker(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    geom = PolygonField()

    def __str__(self):
        return self.title

    # @property
    # def picture_url(self):
    #     return self.picture.url
