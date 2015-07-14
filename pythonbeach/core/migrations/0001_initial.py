# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pythonbeach.core.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoiadores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(verbose_name='Apoiador', max_length=100)),
                ('image', models.ImageField(verbose_name='Imagem', upload_to=pythonbeach.core.models.Apoiador.image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Palestrante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(verbose_name='Nome Palestrante', max_length=100)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('image', models.ImageField(verbose_name='Imagem', upload_to=pythonbeach.core.models.Palestrante.image_path)),
            ],
        ),
    ]
