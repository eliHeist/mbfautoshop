# Generated by Django 5.1.6 on 2025-04-25 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("parts", "0006_alter_part_break_even_price_alter_part_selling_price"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="partcategory",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
    ]
