# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-02-05 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Course', verbose_name='所属课程'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_img',
            field=models.ImageField(upload_to='image', verbose_name='课程图片'),
        ),
    ]
