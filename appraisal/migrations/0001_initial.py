# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-25 15:25
from __future__ import unicode_literals

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
            name='Appraisal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(default='', max_length=300)),
                ('rank', models.SmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('appraisal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='appraisal.Appraisal')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.IntegerField(choices=[(0, 'N/A'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')], default=0, verbose_name='Is the user competent in what he/she does?')),
                ('q2', models.IntegerField(choices=[(0, 'N/A'), (1, 'Rarely Achieves Expectations '), (2, 'Sometimes Achieves Expectations'), (3, 'Fully Achieves Expectations'), (4, 'Fully Achieves and Occasionally Exceeds Expectations\t'), (5, 'Consistently Exceeds Expectations')], default=0, verbose_name='Accomplishments - the extent to which the employee meets expectations in performing the job functions of his/her position as defined in documentation such as the PDQ. ')),
                ('q3', models.IntegerField(choices=[(0, 'N/A'), (1, 'Rarely Achieves Expectations '), (2, 'Sometimes Achieves Expectations'), (3, 'Fully Achieves Expectations'), (4, 'Fully Achieves and Occasionally Exceeds Expectations\t'), (5, 'Consistently Exceeds Expectations')], default=0, verbose_name="Service & Relationships - the extent to which the employee's behaviors are directed toward fostering positive working relationships in a diverse workplace, respect for one's fellow workers, and cooperation with students, customers, and visitors. ")),
                ('q4', models.IntegerField(choices=[(0, 'N/A'), (1, 'Rarely Achieves Expectations '), (2, 'Sometimes Achieves Expectations'), (3, 'Fully Achieves Expectations'), (4, 'Fully Achieves and Occasionally Exceeds Expectations\t'), (5, 'Consistently Exceeds Expectations')], default=0, verbose_name='Accountability & Dependability - the extent to which the employee contributes to the effectiveness of the department and the overall mission of the University. ')),
                ('q5', models.IntegerField(choices=[(0, 'N/A'), (1, 'Rarely Achieves Expectations '), (2, 'Sometimes Achieves Expectations'), (3, 'Fully Achieves Expectations'), (4, 'Fully Achieves and Occasionally Exceeds Expectations\t'), (5, 'Consistently Exceeds Expectations')], default=0, verbose_name='Adaptability & Flexibility - the extent to which the employee exhibits openness to new ideas, programs, systems, and/or structures. ')),
                ('q6', models.IntegerField(choices=[(0, 'N/A'), (1, 'Rarely Achieves Expectations '), (2, 'Sometimes Achieves Expectations'), (3, 'Fully Achieves Expectations'), (4, 'Fully Achieves and Occasionally Exceeds Expectations\t'), (5, 'Consistently Exceeds Expectations')], default=0, verbose_name='Decision Making & Problem Solving - the extent to which the employee makes sound and logical job-related decisions that are in the best interest of the company ')),
                ('q7', models.IntegerField(choices=[(0, 'N/A'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')], default=0, verbose_name='Atendance and Punctuality to work ')),
                ('q8', models.IntegerField(choices=[(0, 'N/A'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')], default=0, verbose_name='Customer service ')),
                ('q9', models.IntegerField(choices=[(0, 'N/A'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')], default=0, verbose_name='Planning and organization of work ')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('superior_comment', models.TextField(default='')),
                ('hr_comment', models.TextField(default='')),
                ('total', models.IntegerField(default='0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appraisal',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='appraisal.Employee'),
        ),
        migrations.AddField(
            model_name='appraisal',
            name='superior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='appraisal.Employee'),
        ),
    ]
