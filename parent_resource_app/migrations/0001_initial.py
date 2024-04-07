# Generated by Django 4.2 on 2024-04-07 15:51

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, null=True)),
                ('about', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('age_group', multiselectfield.db.fields.MultiSelectField(choices=[('0', '0-1 years'), ('1', '1-2 years'), ('2', '2-3 years'), ('3', '3-4 years'), ('4', '4-5 years'), ('5', '5-6 years'), ('6', '6-7 years'), ('7', '7-8 years'), ('8', '8-9 years'), ('9', '9-10 years'), ('10', '10-11 years'), ('11', '11-12 years'), ('12', '12-13 years'), ('13', '13-14 years'), ('14', '14-15 years'), ('15', '15-16 years'), ('16+', '16 or older'), ('P', 'For Parents'), ('All', 'All ages')], max_length=3)),
                ('service_type', models.CharField(choices=[('Fam-Fun', 'Family Fun'), ('Health', 'Health and Well-being'), ('Finance', 'Benefits or Financial Aid')], max_length=200, verbose_name='Type of Event')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(null=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(null=True, verbose_name='End Date')),
                ('location', models.CharField(max_length=200, null=True, verbose_name='Location')),
                ('group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='parent_resource_app.group')),
            ],
        ),
    ]
