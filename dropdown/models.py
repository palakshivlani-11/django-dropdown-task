from django.db import models

# Create your models here.

class Country(models.Model):
    name= models.CharField(max_length=50,)
    def __str__(self):
        return self.name
class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,)
    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name




class UserResponses(models.Model):
    name = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)