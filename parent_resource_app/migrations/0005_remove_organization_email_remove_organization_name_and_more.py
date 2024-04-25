# Generated by Django 4.2 on 2024-04-25 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parent_resource_app', '0004_remove_organizationtranslation_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='email',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='name',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='user',
        ),
        migrations.AddField(
            model_name='organizationtranslation',
            name='email',
            field=models.EmailField(default=1, max_length=200, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationtranslation',
            name='name',
            field=models.CharField(default=1, max_length=200, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationtranslation',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='organizationtranslation',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
