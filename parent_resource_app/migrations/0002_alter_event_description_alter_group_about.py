# Generated by Django 4.2 on 2024-04-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent_resource_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='group',
            name='about',
            field=models.TextField(max_length=200),
        ),
    ]
