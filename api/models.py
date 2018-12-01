from django.db import models
from jsonfield import JSONField

class Offer(models.Model):
    product = models.CharField(max_length=30, primary_key=True)
    menulink = models.CharField(max_length=255)
    hilite = models.FloatField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return "%s" % self.product

class Analytics(models.Model):
    user = models.CharField(max_length=255)
    action = models.CharField(max_length=20)
    data = JSONField()

    def __str__(self):
        return "%s [%s]" % (self.user, self.action) 