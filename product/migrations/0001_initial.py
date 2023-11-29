# Generated by Django 4.2.7 on 2023-11-21 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('features', models.TextField(blank=True)),
                ('personalization', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('collection', models.CharField(choices=[('F', 'Folder'), ('O', 'Pen Organizer'), ('P', 'Planner')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('length', models.FloatField(default=0)),
                ('width', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
            ],
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='PenOrganizer',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('slots', models.IntegerField(default=0)),
            ],
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('length', models.FloatField(default=0)),
                ('width', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
            ],
            bases=('product.product',),
        ),
    ]