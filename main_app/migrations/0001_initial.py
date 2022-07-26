# Generated by Django 4.0.6 on 2022-07-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity_available', models.IntegerField()),
                ('product_description', models.TextField(max_length=250)),
            ],
        ),
    ]
