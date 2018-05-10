# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0010_auto_20180508_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='titulo',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
