# Generated by Django 2.2.28 on 2023-05-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_answer_lobby'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='score1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='score2',
            field=models.IntegerField(default=0),
        ),
    ]
