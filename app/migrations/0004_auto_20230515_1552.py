# Generated by Django 2.2.28 on 2023-05-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230515_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='q1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q3',
            field=models.IntegerField(null=True),
        ),
    ]
