from django.db import models
from company.models import Company


class Lawyer(models.Model):
    """
    Representação do perfil do advogado.

    Atributos:
        company: A companhia a qual o advogado está associado.
        name: O nome do advogado.
        username: O username definido pelo advogado.
        bio: A biografia do advogado.

    Métodos:
        __str__: Retorna uma repreesentação em string do nome do advogado.
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=500, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
