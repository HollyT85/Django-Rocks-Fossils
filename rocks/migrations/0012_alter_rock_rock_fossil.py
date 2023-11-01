# Generated by Django 3.2.21 on 2023-11-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocks', '0011_rename_user_rock_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rock',
            name='rock_fossil',
            field=models.CharField(choices=[('ROCK', 'rock'), ('FOSSIL', 'fossil')], default='fossil', max_length=6),
        ),
    ]
