# Generated by Django 5.1.6 on 2025-04-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchases", "0001_initial"),
        ("stock", "0005_remove_stocktransaction_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="re_stocks",
            field=models.ManyToManyField(blank=True, to="stock.stocktransaction"),
        ),
    ]
