# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dispute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1024)),
                ('u1', models.ForeignKey(to='mitm.user')),
            ],
        ),
    ]
