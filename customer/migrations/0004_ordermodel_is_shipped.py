# Generated by Django 3.1 on 2022-06-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]
