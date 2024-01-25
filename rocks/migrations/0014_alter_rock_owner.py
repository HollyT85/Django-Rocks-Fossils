# Generated by Django 3.2.21 on 2024-01-25 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rocks', '0013_alter_rock_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rock',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
