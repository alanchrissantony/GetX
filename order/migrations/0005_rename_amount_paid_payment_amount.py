# Generated by Django 5.0.2 on 2024-05-20 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_options_order_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='amount_paid',
            new_name='amount',
        ),
    ]
