# Generated by Django 4.0.10 on 2024-02-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monappli', '0010_alter_client_client_ip_alter_hit_referer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_url',
            field=models.URLField(),
        ),
    ]
