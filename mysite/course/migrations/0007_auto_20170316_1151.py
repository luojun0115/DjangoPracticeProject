# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-16 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_remove_content_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='file',
            name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.RemoveField(
            model_name='text',
            name='user',
        ),
        migrations.RemoveField(
            model_name='video',
            name='user',
        ),
        migrations.AddField(
            model_name='lesson',
            name='attach',
            field=models.FileField(blank=True, upload_to='attachs'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.FileField(default=1, upload_to='videos'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]