# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('giver_name', models.CharField(blank=True, max_length=200)),
                ('workagain', models.IntegerField()),
                ('didenjoy', models.TextField(blank=True)),
                ('didnotenjoy', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('public_id', models.CharField(max_length=10, unique=True)),
                ('token', models.CharField(max_length=20)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('asker_email', models.CharField(max_length=200)),
                ('asker_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='feedback',
            name='questionnaire',
            field=models.ForeignKey(to='feedback.Questionnaire'),
            preserve_default=True,
        ),
    ]
