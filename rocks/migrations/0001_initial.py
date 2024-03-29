# Generated by Django 3.2.21 on 2023-09-06 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('extra_info', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('era', models.CharField(blank=True, max_length=255, null=True)),
                ('tools_used', models.TextField(blank=True, null=True)),
                ('date_found', models.DateTimeField(blank=True, null=True)),
                ('prepped_self', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='../default_post_i7zqny', upload_to='images/')),
                ('finished_image', models.ImageField(blank=True, default='../default_post_i7zqny', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
    ]
