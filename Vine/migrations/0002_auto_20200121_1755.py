# Generated by Django 2.2.9 on 2020-01-21 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinealbum',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vine.Profile'),
        ),
    ]
