# Generated by Django 4.0.5 on 2022-06-07 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('isbn', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traking_id', models.CharField(max_length=100)),
                ('shipment_id', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.user')),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consignment', models.CharField(max_length=100)),
                ('shipment_id', models.CharField(max_length=100)),
                ('created_at', models.CharField(max_length=100)),
                ('Shipment_state', models.CharField(max_length=100)),
                ('tracking_url', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.user')),
            ],
        ),
        migrations.CreateModel(
            name='AddressDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_add_line_1', models.CharField(max_length=100)),
                ('sender_add_line_2', models.CharField(max_length=100)),
                ('receiver_add_line_1', models.CharField(max_length=100)),
                ('receiver_add_line_2', models.CharField(max_length=100)),
                ('consignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.consignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.user')),
            ],
        ),
    ]