# Generated by Django 3.2.21 on 2023-10-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocks', '0007_auto_20231003_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rock',
            name='date_found',
            field=models.DateField(blank=True, null=True),
        ),
    ]