# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0005_auto_20180504_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='museos',
        ),
        migrations.AddField(
            model_name='usuario',
            name='museos',
            field=models.ForeignKey(to='museos.Museo', default=0),
            preserve_default=False,
        ),
    ]
