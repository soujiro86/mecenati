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
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(related_name=b'portfolio_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('portrait', models.ImageField(upload_to=b'')),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=400)),
                ('district', models.CharField(max_length=400)),
                ('country', models.CharField(max_length=400)),
                ('artist', models.BooleanField(default=False)),
                ('patron', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill_set',
            field=models.ManyToManyField(related_name=b'skilled_profile_set', null=True, to='profiles.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(related_name=b'profile_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
