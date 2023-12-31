# Generated by Django 4.2.7 on 2023-12-22 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IPsecVPN_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('comments', models.TextField()),
                ('status', models.CharField(max_length=50)),
                ('incoming_core', models.CharField(max_length=50)),
                ('outgoing_core', models.CharField(max_length=50)),
                ('p2name', models.CharField(max_length=50)),
                ('incoming_tunnel', models.CharField(max_length=50)),
                ('outgoing_tunnel', models.CharField(max_length=50)),
                ('interface', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='APIUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_time', models.FloatField()),
                ('access_token', models.CharField(max_length=255)),
                ('expires_in', models.CharField(max_length=255)),
                ('token_type', models.CharField(max_length=255)),
                ('scope', models.CharField(max_length=255)),
                ('refresh_token', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
