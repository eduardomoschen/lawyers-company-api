from django.db import models
from company.models import Company


class Lawyer(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=500, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username
