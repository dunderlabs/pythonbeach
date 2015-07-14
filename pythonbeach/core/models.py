from django.db import models


class Palestrante(models.Model):

    def image_path(self, filename):
        return 'perfil/{}'.format(filename)

    nome = models.CharField('Nome Palestrante', max_length=100)
    descricao = models.TextField('Descrição')
    image = models.ImageField('Imagem', upload_to=image_path)

    def __str__(self):
        return self.nome


class Apoiador(models.Model):

    def image_path(self, filename):
        return 'apoiador/{}'.format(filename)

    nome = models.CharField('Apoiador', max_length=100)
    image = models.ImageField('Imagem', upload_to=image_path)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Apoiador'
        verbose_name_plural = 'Apoiadores'
