from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Palestrante(models.Model):

    def image_path(self, filename):
        return 'perfil/{}'.format(filename)

    nome = models.CharField('Nome Palestrante', max_length=100)
    descricao = models.TextField('Descrição')
    avatar_thumbnail = ProcessedImageField(
        upload_to=image_path,
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 60},
        blank=True
    )

    def __str__(self):
        return self.nome


class Apoiador(models.Model):

    def image_path(self, filename):
        return 'apoiador/{}'.format(filename)

    nome = models.CharField('Apoiador', max_length=100)
    logo_thumbnail = ProcessedImageField(
        upload_to=image_path,
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 60},
        blank=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Apoiador'
        verbose_name_plural = 'Apoiadores'
