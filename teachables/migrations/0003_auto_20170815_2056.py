# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachables', '0002_subtopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('order', models.IntegerField(default=0)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='subtopic',
            old_name='Parent',
            new_name='parent',
        ),
        migrations.AddField(
            model_name='step',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachables.Subtopic'),
        ),
    ]