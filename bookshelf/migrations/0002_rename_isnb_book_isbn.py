# Generated by Django 4.2.7 on 2023-11-25 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isnb',
            new_name='isbn',
        ),
    ]
