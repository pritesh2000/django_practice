# Generated by Django 4.0.3 on 2022-04-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('serial_no', models.IntegerField()),
                ('site', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]