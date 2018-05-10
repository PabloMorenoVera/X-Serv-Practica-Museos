# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0011_usuario_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='direccion',
            field=models.CharField(max_length=128, default=''),
            preserve_default=False,
        ),
    ]
