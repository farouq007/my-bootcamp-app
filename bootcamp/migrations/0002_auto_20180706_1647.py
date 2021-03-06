# Generated by Django 2.0.7 on 2018-07-06 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bootcamp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=500)),
                ('picture', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='user',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='reply',
        ),
        migrations.AddField(
            model_name='articles',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Profiles',
        ),
    ]
