# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('id_museo', models.IntegerField()),
                ('texto', models.TextField(null=True, blank=True)),
                ('usuario', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Museo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('id_museo', models.IntegerField()),
                ('usuario', models.CharField(max_length=128)),
                ('comentarios', models.ForeignKey(to='museos.Comentario')),
            ],
        ),
    ]
