# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pythonbeach.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150714_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apoiador',
            name='logo_thumbnail',
        ),
        migrations.AddField(
            model_name='apoiador',
            name='logo',
            field=models.ImageField(blank=True, upload_to=pythonbeach.core.models.Apoiador.image_path),
        ),
    ]
