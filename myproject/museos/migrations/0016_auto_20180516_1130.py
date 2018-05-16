# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0015_auto_20180516_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='museo',
            old_name='accesibilidad',
            new_name='ACCESIBILIDAD',
        ),
        migrations.RenameField(
            model_name='museo',
            old_name='url',
            new_name='CONTENT_URL',
        ),
        migrations.RemoveField(
            model_name='museo',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='museo',
            name='distrito',
        ),
        migrations.RemoveField(
            model_name='museo',
            name='nombre',
        ),
        migrations.AddField(
            model_name='museo',
            name='BARRIO',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='CLASE_VIAL',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='CODIGO_POSTAL',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='COORDENADA_X',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='COORDENADA_Y',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='DESCRIPCION',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='DISTRITO',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='EMAIL',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='FAX',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='HORARIO',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='ID_ENTIDAD',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='LATITUD',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='LOCALIDAD',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='LONGITUD',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='NOMBRE',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='NOMBRE_VIA',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='NUM',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='PROVINCIA',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='TELEFONO',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='TIPO_NUM',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museo',
            name='TRANSPORTE',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
