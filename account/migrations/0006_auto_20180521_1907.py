# Generated by Django 2.0.5 on 2018-05-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180520_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
