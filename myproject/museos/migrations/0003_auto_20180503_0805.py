# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0002_auto_20180503_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='museo',
            name='usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='museos',
            field=models.ManyToManyField(to='museos.Museo'),
        ),
    ]
