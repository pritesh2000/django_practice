# Generated by Django 4.0.3 on 2022-03-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
