# Generated by Django 4.1.5 on 2023-02-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_alter_order_status_alter_order_total_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='def.png', null=True, upload_to=''),
        ),
    ]
