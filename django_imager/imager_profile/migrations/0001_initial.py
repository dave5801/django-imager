# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-17 00:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=180)),
                ('location', models.CharField(max_length=50)),
                ('commission', models.FloatField(blank=True, max_length=20, null=True)),
                ('camera', multiselectfield.db.fields.MultiSelectField(choices=[('NikonD3300', 'NikonD3300'), ('CanonT6i', 'CanonT6i'), ('Canon5dMarkIII', 'Canon5dMarkIII'), ('SonyAlphaA99II', 'SonyAlphaA99II')], default='CanonT6i', max_length=20)),
                ('services', multiselectfield.db.fields.MultiSelectField(choices=[('Ultimate-Service Pack', '20 photos, provided lighting equipment, additional photo editing post-production.'), ('Mega-Service Pack', '15 photos, provided lighting equipment, 5 free prints of your choice.'), ('Basic-Service Pack', '10 photos, 3 free prints of your choice.')], default='Mega-Service Pack', max_length=2000)),
                ('bio', models.TextField(max_length=2000)),
                ('phone', models.CharField(max_length=14)),
                ('photo_styles', multiselectfield.db.fields.MultiSelectField(choices=[("70's", 'Classic retro style with filters to match.'), ('Noir', 'Bold black and white photos.'), ('Bokeh', 'Blurry background with subject in focus.'), ('Studio', 'Profile shots with bright lighting and white backdrop.'), ('Standard', 'Regular shots with no filters.')], default='Standard', max_length=400)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
