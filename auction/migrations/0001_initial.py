# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('budget', models.DecimalField(max_digits=10, decimal_places=2)),
                ('height', models.IntegerField()),
                ('length', models.IntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('release_date', models.DateField(auto_now=True)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=400)),
                ('district', models.CharField(max_length=400)),
                ('country', models.CharField(max_length=400)),
                ('owner', models.ForeignKey(related_name=b'auction_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('draft', models.ImageField(upload_to=b'')),
                ('budget', models.DecimalField(max_digits=10, decimal_places=2)),
                ('estimated_time', models.IntegerField()),
                ('chosen', models.BooleanField(default=False)),
                ('bidder', models.ForeignKey(related_name=b'bid_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('bid', models.OneToOneField(related_name=b'feedback_set', to='auction.Bid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('estimated_time', models.IntegerField()),
                ('checked', models.BooleanField(default=False)),
                ('auction', models.ForeignKey(related_name=b'milestone_set', to='auction.Auction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
