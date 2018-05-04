# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0003_auto_20180503_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='color',
            field=models.CharField(max_length=32, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='letra',
            field=models.CharField(max_length=64, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(to='museos.Usuario'),
        ),
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
