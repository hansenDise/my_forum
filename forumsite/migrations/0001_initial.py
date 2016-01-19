# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('catetoryid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentid', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('pushtime', models.DateField(default=datetime.datetime(2016, 1, 19, 9, 48, 59, 904000))),
            ],
            options={
                'ordering': ['pushtime'],
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('threadid', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('pushtime', models.DateTimeField(default=datetime.datetime(2016, 1, 19, 9, 48, 59, 903000))),
                ('commentsCount', models.IntegerField(default=0)),
                ('categoryid', models.ForeignKey(to='forumsite.Category', db_column=b'categoryid')),
                ('userid', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'userid')),
            ],
            options={
                'ordering': ['-pushtime'],
                'db_table': 'Thread',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='threadid',
            field=models.ForeignKey(to='forumsite.Thread', db_column=b'threadid'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userid',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'userid'),
        ),
    ]
