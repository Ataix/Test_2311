# Generated by Django 4.2.7 on 2023-11-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publish_year', models.IntegerField()),
                ('isnb', models.IntegerField(unique=True)),
            ],
        ),
    ]