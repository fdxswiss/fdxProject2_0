# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-27 20:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fdx_mail', '0002_firmeneintrag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firmeneintrag',
            old_name='firmaName',
            new_name='firma',
        ),
        migrations.RenameField(
            model_name='firmeneintrag',
            old_name='nameAnsprechperson',
            new_name='name',
        ),
    ]
