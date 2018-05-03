# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='id_museo',
        ),
        migrations.RemoveField(
            model_name='museo',
            name='comentarios',
        ),
        migrations.RemoveField(
            model_name='museo',
            name='id_museo',
        ),
        migrations.AddField(
            model_name='comentario',
            name='museo',
            field=models.ForeignKey(to='museos.Museo', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='distrito',
            field=models.CharField(max_length=128, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='nombre',
            field=models.CharField(max_length=128, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='url',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]
