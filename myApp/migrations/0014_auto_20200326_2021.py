# Generated by Django 2.2.6 on 2020-03-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_auto_20200326_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='sname',
            field=models.CharField(max_length=20),
        ),
    ]