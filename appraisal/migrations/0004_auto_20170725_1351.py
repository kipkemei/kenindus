# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-25 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appraisal', '0003_question_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
