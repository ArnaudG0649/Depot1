# Generated by Django 4.0.10 on 2024-02-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monappli', '0013_alter_hit_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hit',
            name='timestamp',
            field=models.CharField(max_length=50),
        ),
    ]
