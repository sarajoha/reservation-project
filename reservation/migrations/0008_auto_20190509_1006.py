# Generated by Django 2.2 on 2019-05-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_reservation_duration_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='duration',
            field=models.DurationField(blank=True),
        ),
    ]
