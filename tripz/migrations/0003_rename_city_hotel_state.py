# Generated by Django 5.0.3 on 2024-04-24 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripz', '0002_hotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='city',
            new_name='state',
        ),
    ]
