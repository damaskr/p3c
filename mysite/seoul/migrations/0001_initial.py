# Generated by Django 2.2.7 on 2019-11-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afterseoul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=10)),
                ('employ_type', models.CharField(max_length=10)),
                ('school_url', models.CharField(max_length=100)),
            ],
        ),
    ]
