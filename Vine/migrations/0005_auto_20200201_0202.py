# Generated by Django 2.2.9 on 2020-01-31 17:02

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('Vine', '0004_auto_20200131_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='vine',
            name='dislikes',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), default='None2', max_length=66, size=None),
        ),
        migrations.AddField(
            model_name='vine',
            name='likes',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), default='None', max_length=66, size=None),
        ),
    ]
