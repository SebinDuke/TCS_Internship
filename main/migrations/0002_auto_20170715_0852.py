# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user_address'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('delivered', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='books',
            name='no_of_pages',
        ),
        migrations.AddField(
            model_name='books',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='books',
            name='varification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Books'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]
