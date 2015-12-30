from django.db import models

class Continent(models.Model):
    """ Write your answer in 7.1 here. """
    name = models.CharField(max_length=255,unique=True)
    code = models.CharField(max_length=255,unique=True)

    class Meta:
        ordering = ["name"]


class Country(models.Model):
    """ Write your answer in 7.1 here. """
    name = models.CharField(max_length=255,unique=True)
    capital = models.CharField(max_length=255)
    code =  models.CharField(max_length=255,unique=True)
    population= models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    continent = models.ForeignKey(Continent, related_name="countries")

    class Meta:
        ordering = ["name"]
