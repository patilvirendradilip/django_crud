# Generated by Django 4.0.2 on 2022-03-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
