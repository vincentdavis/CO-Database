# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 09:50
from __future__ import unicode_literals

import datetime
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
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_year', models.IntegerField(default=None)),
                ('tax_type', models.CharField(max_length=64)),
                ('effective_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalOwner',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dba', models.BooleanField(default=False)),
                ('ownico', models.BooleanField(default=False)),
                ('other', models.CharField(default=None, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical owner',
            },
        ),
        migrations.CreateModel(
            name='HistoricalOwnerAddress',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('idhash', models.CharField(db_index=True, editable=False, max_length=128)),
                ('street1', models.CharField(default=None, max_length=255, null=True)),
                ('street2', models.CharField(default=None, max_length=255, null=True)),
                ('city', models.CharField(default=None, max_length=255, null=True)),
                ('state', models.CharField(default=None, max_length=255, null=True)),
                ('zipcode', models.IntegerField(default=None, null=True)),
                ('zip4', models.IntegerField(default=None, null=True)),
                ('standardized', models.CharField(default=None, max_length=255, null=True)),
                ('tiger_line_id', models.CharField(default=None, max_length=16, null=True)),
                ('tiger_line_side', models.CharField(choices=[('L', 'Left'), ('R', 'Right')], default=None, max_length=1, null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical owner address',
            },
        ),
        migrations.CreateModel(
            name='HistoricalOwnerProperties',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical owner properties',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProperty',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('parid', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical property',
            },
        ),
        migrations.CreateModel(
            name='HistoricalPropertyAddress',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('idhash', models.CharField(db_index=True, editable=False, max_length=128)),
                ('street1', models.CharField(default=None, max_length=255, null=True)),
                ('street2', models.CharField(default=None, max_length=255, null=True)),
                ('city', models.CharField(default=None, max_length=255, null=True)),
                ('state', models.CharField(default=None, max_length=255, null=True)),
                ('zipcode', models.IntegerField(default=None, null=True)),
                ('zip4', models.IntegerField(default=None, null=True)),
                ('standardized', models.CharField(default=None, max_length=255, null=True)),
                ('tiger_line_id', models.CharField(default=None, max_length=16, null=True)),
                ('tiger_line_side', models.CharField(choices=[('L', 'Left'), ('R', 'Right')], default=None, max_length=1, null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical property address',
            },
        ),
        migrations.CreateModel(
            name='LienAuction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('name', models.CharField(max_length=255)),
                ('tax_year', models.IntegerField()),
                ('winning_bid', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dba', models.BooleanField(default=False)),
                ('ownico', models.BooleanField(default=False)),
                ('other', models.CharField(default=None, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idhash', models.CharField(editable=False, max_length=128, unique=True)),
                ('street1', models.CharField(default=None, max_length=255, null=True)),
                ('street2', models.CharField(default=None, max_length=255, null=True)),
                ('city', models.CharField(default=None, max_length=255, null=True)),
                ('state', models.CharField(default=None, max_length=255, null=True)),
                ('zipcode', models.IntegerField(default=None, null=True)),
                ('zip4', models.IntegerField(default=None, null=True)),
                ('standardized', models.CharField(default=None, max_length=255, null=True)),
                ('tiger_line_id', models.CharField(default=None, max_length=16, null=True)),
                ('tiger_line_side', models.CharField(choices=[('L', 'Left'), ('R', 'Right')], default=None, max_length=1, null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='prop.Owner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OwnerProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prop.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parid', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idhash', models.CharField(editable=False, max_length=128, unique=True)),
                ('street1', models.CharField(default=None, max_length=255, null=True)),
                ('street2', models.CharField(default=None, max_length=255, null=True)),
                ('city', models.CharField(default=None, max_length=255, null=True)),
                ('state', models.CharField(default=None, max_length=255, null=True)),
                ('zipcode', models.IntegerField(default=None, null=True)),
                ('zip4', models.IntegerField(default=None, null=True)),
                ('standardized', models.CharField(default=None, max_length=255, null=True)),
                ('tiger_line_id', models.CharField(default=None, max_length=16, null=True)),
                ('tiger_line_side', models.CharField(choices=[('L', 'Left'), ('R', 'Right')], default=None, max_length=1, null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='prop.Property')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='property',
            unique_together=set([('parid', 'county')]),
        ),
        migrations.AddField(
            model_name='ownerproperties',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prop.Property'),
        ),
        migrations.AddField(
            model_name='owner',
            name='properties',
            field=models.ManyToManyField(blank=True, default=list, through='prop.OwnerProperties', to='prop.Property'),
        ),
        migrations.AddField(
            model_name='lienauction',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prop.Property'),
        ),
        migrations.AddField(
            model_name='historicalpropertyaddress',
            name='property',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='prop.Property'),
        ),
        migrations.AddField(
            model_name='historicalownerproperties',
            name='owner',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='prop.Owner'),
        ),
        migrations.AddField(
            model_name='historicalownerproperties',
            name='property',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='prop.Property'),
        ),
        migrations.AddField(
            model_name='historicalowneraddress',
            name='owner',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='prop.Owner'),
        ),
        migrations.AddField(
            model_name='account',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prop.Property'),
        ),
        migrations.AlterUniqueTogether(
            name='lienauction',
            unique_together=set([('property', 'tax_year')]),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('property', 'tax_year', 'tax_type', 'effective_date', 'amount', 'balance')]),
        ),
    ]
