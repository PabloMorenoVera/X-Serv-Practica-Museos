# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0013_auto_20180511_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='titulo',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
