# Generated by Django 2.0.6 on 2018-07-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0005_feeds'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]