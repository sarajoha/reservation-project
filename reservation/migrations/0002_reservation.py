# Generated by Django 2.2 on 2019-04-25 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('duration', models.DurationField()),
                ('end_time', models.TimeField()),
                ('motive', models.CharField(choices=[('SU', 'Stand Up'), ('CL', 'Clase')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservation.User')),
            ],
        ),
    ]
