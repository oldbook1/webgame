# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20160610_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='number_room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_number', models.IntegerField(default=123, unique=True)),
                ('ball', models.IntegerField()),
                ('strike', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='number_room1',
        ),
        migrations.DeleteModel(
            name='number_room10',
        ),
        migrations.DeleteModel(
            name='number_room2',
        ),
        migrations.DeleteModel(
            name='number_room3',
        ),
        migrations.DeleteModel(
            name='number_room4',
        ),
        migrations.DeleteModel(
            name='number_room5',
        ),
        migrations.DeleteModel(
            name='number_room6',
        ),
        migrations.DeleteModel(
            name='number_room7',
        ),
        migrations.DeleteModel(
            name='number_room8',
        ),
        migrations.DeleteModel(
            name='number_room9',
        ),
        migrations.AddField(
            model_name='player',
            name='cnt',
            field=models.IntegerField(default=1, unique=True),
        ),
        migrations.AddField(
            model_name='player_num',
            name='cnt',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]