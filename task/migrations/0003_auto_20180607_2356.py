# Generated by Django 2.0.5 on 2018-06-07 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20180605_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='validator',
            field=models.ForeignKey(on_delete=models.SET('deleted'), related_name='task_validator', to='account.Employee'),
        ),
    ]
