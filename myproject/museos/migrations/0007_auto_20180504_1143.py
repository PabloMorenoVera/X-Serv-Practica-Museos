# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0006_auto_20180504_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='museos',
        ),
        migrations.AddField(
            model_name='usuario',
            name='museos',
            field=models.ManyToManyField(to='museos.Museo'),
        ),
    ]
