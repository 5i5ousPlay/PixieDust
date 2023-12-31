# Generated by Django 4.2.7 on 2023-11-21 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('delivery_address', models.CharField(max_length=255)),
                ('schedule', models.DateTimeField()),
                ('amount_due', models.FloatField(default=0, null=True)),
                ('gift', models.BooleanField(default=False)),
                ('recepient', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('total', models.FloatField(default=0)),
                ('color', models.CharField(choices=[('RED', 'Red'), ('ORANGE', 'Orange'), ('YELLOW', 'Yellow'), ('GREEN', 'Green'), ('BLUE', 'Blue'), ('PURPLE', 'Purple'), ('PINK', 'Pink'), ('BLACK', 'Black')], max_length=25)),
                ('personalization', models.CharField(blank=True, max_length=255)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='product.product')),
            ],
        ),
    ]
