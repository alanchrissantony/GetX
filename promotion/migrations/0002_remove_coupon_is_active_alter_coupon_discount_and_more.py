# Generated by Django 5.0.2 on 2024-05-19 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.FloatField(),
        ),
    ]
