# Generated by Django 4.1.3 on 2022-11-18 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_team_email_team_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('Service', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Prise de RDV',
                'verbose_name_plural': 'Prises de RDV',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('sujet', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Prise de RDV',
                'verbose_name_plural': 'Prises de RDV',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=True)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'abonnement',
                'verbose_name_plural': 'abonnement',
            },
        ),
    ]