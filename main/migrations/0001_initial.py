# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=80, unique=True)),
                ('auth_name', models.CharField(max_length=40)),
                ('points', models.IntegerField(default=20)),
                ('no_of_pages', models.IntegerField(default=0)),
                ('no_of_copies', models.IntegerField(default=0)),
            ],
        ),
    ]