# Generated by Django 2.0.7 on 2018-07-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0002_auto_20180706_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='userPics'),
        ),
    ]
