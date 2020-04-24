# Generated by Django 3.0.4 on 2020-04-08 10:09

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('secret_key', models.CharField(max_length=128, unique=True)),
                ('app_key', models.CharField(max_length=256, unique=True)),
                ('redirect_urls', models.TextField()),
            ],
            options={
                'db_table': 'apps',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token', models.CharField(db_index=True, max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(null=True)),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='auth.Apps')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='users.User')),
            ],
            options={
                'db_table': 'sessions',
            },
        ),
    ]