from django.contrib import admin
from .models import Lawyer


@admin.register(Lawyer)
class LawyreAdmin(admin.ModelAdmin):
    fields = ('username', 'bio')
