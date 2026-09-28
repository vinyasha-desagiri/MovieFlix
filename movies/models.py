from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    genre = models.CharField(max_length=100)

    release_year = models.IntegerField()

    rating = models.DecimalField(max_digits=3, decimal_places=1)

    poster = models.URLField()

    banner = models.URLField()

    def __str__(self):
        return self.title