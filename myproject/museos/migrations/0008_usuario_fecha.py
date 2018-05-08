# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0007_auto_20180504_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2018, 5, 8, 9, 40, 32, 406073, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
