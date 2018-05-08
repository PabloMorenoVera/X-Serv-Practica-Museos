# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0008_usuario_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='Accesibilidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
