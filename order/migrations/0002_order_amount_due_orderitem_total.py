# Generated by Django 4.2.7 on 2023-11-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount_due',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]