# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-21 21:45
from __future__ import unicode_literals

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
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('cab_no', models.CharField(max_length=8)),
                ('seats_available', models.PositiveIntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('contact_no', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TravelHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('pickup_location', models.CharField(default='django', max_length=40)),
                ('drop_location', models.CharField(default='node', max_length=40)),
                ('seats_requested', models.PositiveIntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabs.Driver')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabs.Passenger')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
