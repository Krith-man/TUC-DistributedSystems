# Generated by Django 2.1a1 on 2018-06-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UUID', models.CharField(max_length=1024)),
                ('StorageService', models.CharField(max_length=100)),
            ],
        ),
    ]
