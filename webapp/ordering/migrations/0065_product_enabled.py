# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-01 13:17


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0064_productstock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
