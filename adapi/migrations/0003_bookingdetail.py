# Generated by Django 3.1.5 on 2021-05-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adapi', '0002_usermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor_id', models.IntegerField()),
                ('booking_time', models.CharField(max_length=50)),
            ],
        ),
    ]
