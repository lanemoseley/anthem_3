# Generated by Django 3.1.1 on 2020-09-06 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=100),
        ),
    ]
