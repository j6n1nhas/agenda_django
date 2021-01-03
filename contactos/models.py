from django.db import models
from django.utils import timezone


# Create your models here.
class Ver:
    pass


class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Contacto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    apelido = models.CharField('Apelido', max_length=100, blank=True)
    telefone = models.CharField('Telefone', max_length=15, unique=True)
    email = models.EmailField('E-mail', blank=True)
    data_criacao = models.DateTimeField('Data de criação', default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField('Foto', blank=True, upload_to='fotos')

    def __str__(self):
        return self.nome
