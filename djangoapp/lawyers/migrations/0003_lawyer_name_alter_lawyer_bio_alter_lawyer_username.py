# Generated by Django 4.2.7 on 2023-11-12 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyers', '0002_lawyer_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='username',
            field=models.CharField(max_length=500),
        ),
    ]
