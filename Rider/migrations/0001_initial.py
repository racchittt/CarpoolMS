# Generated by Django 3.2.2 on 2022-11-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ride',
            fields=[
                ('userId', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('pickup', models.CharField(max_length=100)),
                ('u_destination', models.CharField(max_length=100)),
            ],
        ),
    ]
