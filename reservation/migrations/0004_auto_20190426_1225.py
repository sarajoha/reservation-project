# Generated by Django 2.2 on 2019-04-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20190426_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
