# Generated by Django 3.1.1 on 2025-02-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
