# Generated by Django 4.0.10 on 2024-04-11 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0004_remove_emailadress_employee_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emailadress',
            fields=[
                ('emailadress_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('interne', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100, null=True)),
                ('mailbox', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('mail_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('timedate', models.DateTimeField()),
                ('path', models.CharField(max_length=1000)),
                ('emailadress_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.emailadress')),
            ],
        ),
        migrations.CreateModel(
            name='To',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailadress_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.emailadress')),
                ('mail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.mail')),
            ],
        ),
        migrations.CreateModel(
            name='Re',
            fields=[
                ('remail_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('mail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.mail')),
            ],
        ),
        migrations.AddField(
            model_name='emailadress',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.employee'),
        ),
        migrations.CreateModel(
            name='Cc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailadress_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.emailadress')),
                ('mail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.mail')),
            ],
        ),
    ]
