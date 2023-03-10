# Generated by Django 3.2.2 on 2022-11-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='drivers',
            fields=[
                ('driverId', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('driver_fname', models.CharField(max_length=100)),
                ('driver_lname', models.CharField(max_length=100)),
                ('st_destination', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('car_model', models.CharField(max_length=20)),
                ('no_of_seats', models.IntegerField(max_length=2)),
            ],
        ),
    ]
