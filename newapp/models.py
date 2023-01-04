from django.db import models


class customer(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.name
