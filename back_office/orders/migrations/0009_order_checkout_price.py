# Generated by Django 4.2.7 on 2023-12-17 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_order_complete_cost_order_total_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='checkout_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
