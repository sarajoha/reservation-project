# Generated by Django 2.2 on 2019-04-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20190426_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='start_time',
        ),
        migrations.AddField(
            model_name='reservation',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
