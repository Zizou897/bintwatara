# Generated by Django 4.1.3 on 2022-11-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_web_opening'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='title1',
            field=models.CharField(default='Pourquoi nous choisir ?', max_length=50),
            preserve_default=False,
        ),
    ]