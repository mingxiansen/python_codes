# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DRM', '0002_book_ebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ebook',
            field=models.FileField(upload_to='tt'),
        ),
    ]