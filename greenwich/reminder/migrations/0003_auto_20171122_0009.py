# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 00:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reminder', '0002_auto_20171119_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='messagelog',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.Event'),
        ),
        migrations.AddField(
            model_name='messagelog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
