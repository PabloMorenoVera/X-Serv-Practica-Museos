# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0009_museo_accesibilidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='museo',
            old_name='Accesibilidad',
            new_name='accesibilidad',
        ),
    ]
