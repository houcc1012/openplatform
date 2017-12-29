# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-19 04:40
from __future__ import unicode_literals

import bixin.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('status', models.CharField(choices=[(b'PENDING', b'PENDING'), (b'SUCCESS', b'SUCCESS')], default=b'PENDING', max_length=32)),
                ('amount', bixin.fields.BixinDecimalField(decimal_places=30, default=0, max_digits=65)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('event_id', models.IntegerField(db_index=True)),
                ('subject', models.CharField(db_index=True, max_length=32)),
                ('content', bixin.fields.JSONField(blank=True, default={}, null=True)),
                ('status', models.CharField(choices=[(b'RECEIVED', b'RECEIVED'), (b'PROCESSED', b'PROCESSED')], db_index=True, default=b'RECEIVED', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('balance', bixin.fields.BixinDecimalField(decimal_places=30, default=0, max_digits=65)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QRSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('expired_at', models.DateTimeField(db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
                ('expired_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('userid', models.IntegerField(unique=True)),
                ('username', models.CharField(blank=True, default=b'', max_length=200, null=True)),
                ('target_id', models.CharField(max_length=32, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('status', models.CharField(choices=[(b'PENDING', b'PENDING'), (b'SENT', b'SENT')], default=b'PENDING', max_length=32)),
                ('amount', bixin.fields.BixinDecimalField(decimal_places=30, default=0, max_digits=65)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdraws', to='bixin.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='qrsession',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bixin.User'),
        ),
        migrations.AddField(
            model_name='fund',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='bixin.User'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit', to='bixin.User'),
        ),
    ]
