# Generated by Django 2.2.6 on 2019-10-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SenkaCalc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senka',
            name='maxBoxNum',
            field=models.IntegerField(null=True),
        ),
    ]
