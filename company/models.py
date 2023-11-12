from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
