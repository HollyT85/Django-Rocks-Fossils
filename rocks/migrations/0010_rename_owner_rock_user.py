# Generated by Django 3.2.21 on 2023-11-01 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rocks', '0009_rock_rock_fossil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rock',
            old_name='owner',
            new_name='user',
        ),
    ]
