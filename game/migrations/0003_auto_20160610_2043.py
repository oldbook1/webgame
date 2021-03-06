# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_player_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='number_room1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='number_room10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='number_room2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='number_room3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='number_room4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='number_room5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='number_room6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='number_room7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='number_room8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='number_room9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=1234, unique=True)),
                ('number_judgment', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='player_num',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_number', models.IntegerField(default=1234, unique=True)),
                ('room', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='nicname',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
