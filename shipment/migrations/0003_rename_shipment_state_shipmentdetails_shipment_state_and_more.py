# Generated by Django 4.0.5 on 2022-06-07 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0002_addressdetails_shipment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipmentdetails',
            old_name='Shipment_state',
            new_name='shipment_state',
        ),
        migrations.RemoveField(
            model_name='shipmentdetails',
            name='user',
        ),
    ]