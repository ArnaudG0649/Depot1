# Generated by Django 4.0.10 on 2024-02-05 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monappli', '0002_remove_hit_client_delete_client_delete_hit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_ip', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=30)),
                ('referer', models.CharField(max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.client')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.page')),
            ],
        ),
    ]
