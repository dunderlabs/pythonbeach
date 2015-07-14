# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import pythonbeach.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150714_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apoiador',
            name='image',
        ),
        migrations.RemoveField(
            model_name='palestrante',
            name='image',
        ),
        migrations.AddField(
            model_name='apoiador',
            name='logo_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(upload_to=pythonbeach.core.models.Apoiador.image_path, blank=True),
        ),
        migrations.AddField(
            model_name='palestrante',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(upload_to=pythonbeach.core.models.Palestrante.image_path, blank=True),
        ),
    ]
