# Generated by Django 4.0.10 on 2024-04-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_delete_re'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailadress',
            name='emailadress_id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
