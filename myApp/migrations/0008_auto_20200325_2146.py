# Generated by Django 2.2.6 on 2020-03-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_auto_20200325_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='grades',
            name='gfilefield',
            field=models.FileField(default=2, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grades',
            name='glasttime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]