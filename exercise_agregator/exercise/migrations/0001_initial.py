# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgfulltext.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=155, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('solution_text', models.TextField(verbose_name='Text solution')),
                ('solution_file', models.FileField(upload_to=b'', null=True, verbose_name='File solution', blank=True)),
                ('search_index', djorm_pgfulltext.fields.VectorField(default=b'', serialize=False, null=True, editable=False, db_index=True)),
                ('user', models.ForeignKey(verbose_name='Created by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
