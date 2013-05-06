from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    menu = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)

    food = models.ForeignKey(Food)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return self.name

