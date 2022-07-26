# Generated by Django 4.0.6 on 2022-07-25 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_orders_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='order date')),
                ('products', models.CharField(max_length=100)),
                ('quantity_purchased', models.IntegerField()),
                ('total', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.AddField(
            model_name='product',
            name='orders',
            field=models.ManyToManyField(to='main_app.order'),
        ),
    ]
