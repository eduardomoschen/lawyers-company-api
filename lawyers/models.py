from django.db import models


class Lawyer(models.Model):
    username = models.CharField(max_length=200)
    bio = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.username
