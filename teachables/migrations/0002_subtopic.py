# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=140)),
                ('intro', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('Parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachables.Topic')),
            ],
        ),
    ]
