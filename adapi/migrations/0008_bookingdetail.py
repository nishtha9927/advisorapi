# Generated by Django 3.1.5 on 2021-05-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adapi', '0007_delete_bookingdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor_id', models.IntegerField(default=0)),
                ('booking_time', models.CharField(max_length=50)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]
