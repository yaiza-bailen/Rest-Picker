from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='images/', null=True)

    def __unicode__(self):
        return self.name

class Town(models.Model):
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
    picture = models.ImageField(upload_to='images/', null=True)
    map = models.ImageField(upload_to='images/', null=True)
    gmap_url = models.CharField(max_length=200, null=True)

    food = models.ForeignKey(Food)
    town = models.ForeignKey(Town)

    STARS = (
        (1,'one'),
        (2,'two'),
        (3,'three'),
        (4,'four'),
    )
    votes = models.IntegerField(choices=STARS, default=4)

    def __unicode__(self):
        return self.name

