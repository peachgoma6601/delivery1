# Generated by Django 4.0.5 on 2022-06-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0003_rename_shipment_state_shipmentdetails_shipment_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trackingdetails',
            old_name='traking_id',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='trackingdetails',
            old_name='Location',
            new_name='orgin',
        ),
        migrations.RemoveField(
            model_name='trackingdetails',
            name='user',
        ),
        migrations.AddField(
            model_name='trackingdetails',
            name='tracking_page_url',
            field=models.CharField(default=True, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trackingdetails',
            name='traking_number',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
