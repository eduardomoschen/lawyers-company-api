from django.contrib import admin
from lawyers.models import Lawyer


@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    ...
