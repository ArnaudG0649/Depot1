# Generated by Django 4.0.10 on 2024-03-05 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_ip', models.GenericIPAddressField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(max_length=50)),
                ('referer', models.URLField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.client')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monappli.page')),
            ],
        ),
    ]
