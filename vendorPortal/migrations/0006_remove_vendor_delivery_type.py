# Generated by Django 3.2.8 on 2021-12-26 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendorPortal', '0005_auto_20211222_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='Delivery_Type',
        ),
    ]
