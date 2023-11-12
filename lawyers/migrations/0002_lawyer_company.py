# Generated by Django 4.2.7 on 2023-11-12 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('lawyers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company'),
        ),
    ]
