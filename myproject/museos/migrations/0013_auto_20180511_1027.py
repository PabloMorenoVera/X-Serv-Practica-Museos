# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0012_museo_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='titulo',
            field=models.CharField(default='', max_length=64),
        ),
    ]
