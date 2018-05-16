# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0014_auto_20180511_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('museo', models.ForeignKey(to='museos.Museo')),
            ],
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='museos',
        ),
        migrations.AddField(
            model_name='favorito',
            name='usuario',
            field=models.ForeignKey(to='museos.Usuario'),
        ),
    ]
