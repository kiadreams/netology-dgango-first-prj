# Generated by Django 5.1.1 on 2024-09-08 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='measurement/photos/'),
        ),
    ]
