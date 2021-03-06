# Generated by Django 3.1.5 on 2021-10-24 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adapi', '0008_bookingdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetail',
            name='advisor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adapi.advisordetail'),
        ),
        migrations.AlterField(
            model_name='bookingdetail',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adapi.usermodel'),
        ),
    ]
