# Generated by Django 4.2 on 2024-04-25 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parent_resource_app', '0005_remove_organization_email_remove_organization_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='event',
            name='price',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
        migrations.AddField(
            model_name='eventtranslation',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='eventtranslation',
            name='organization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='parent_resource_app.organization'),
        ),
        migrations.AddField(
            model_name='eventtranslation',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventtranslation',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]