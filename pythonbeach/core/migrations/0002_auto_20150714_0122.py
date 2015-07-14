# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Apoiadores',
            new_name='Apoiador',
        ),
        migrations.AlterModelOptions(
            name='apoiador',
            options={'verbose_name_plural': 'Apoiadores', 'verbose_name': 'Apoiador'},
        ),
    ]
