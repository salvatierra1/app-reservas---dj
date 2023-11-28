# Generated by Django 4.2.7 on 2023-11-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('dni', models.IntegerField()),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('state', models.BooleanField(default=True)),
            ],
        ),
    ]
