# Generated by Django 4.2.7 on 2023-11-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortiwan_monitor', '0002_vpn_tunnel_delete_tunnel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpn_tunnel',
            name='tun_id',
            field=models.CharField(max_length=255),
        ),
    ]