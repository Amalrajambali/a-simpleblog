# Generated by Django 3.0.9 on 2020-09-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20200925_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read Blog Post....', max_length=255),
        ),
    ]
