# Generated by Django 4.2 on 2024-04-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent_resource_app', '0003_alter_event_age_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
