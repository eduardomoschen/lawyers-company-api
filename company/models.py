from django.db import models


class Company(models.Model):
    """
    Representação da empresa de advogados.

    Atributos:
        name: O nome da empresa.
        bio: Uma descrição da empresa.

    Métodos:
        __str__: Retorna uma representação em string do nome da empresa.
    """

    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
