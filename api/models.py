from django.db import models

class Offer(models.Model):
    product = models.CharField(max_length=30, primary_key=True)
    menulink = models.CharField(max_length=255)
    hilite = models.FloatField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return "%s" % self.product
