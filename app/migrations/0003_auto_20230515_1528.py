# Generated by Django 2.2.28 on 2023-05-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230503_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='q1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='q10',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q11',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q12',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q13',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q14',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q15',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='q3',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='q4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q6',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q7',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q8',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='q9',
            field=models.IntegerField(null=True),
        ),
    ]
