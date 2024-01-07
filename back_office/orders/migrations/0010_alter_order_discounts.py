# Generated by Django 4.2.7 on 2023-12-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_checkout_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discounts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
