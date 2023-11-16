from rest_framework.serializers import ModelSerializer
from lawyers.models import Lawyer
from company.serializers import CompanySerializer


class LawyerSerializer(ModelSerializer):
    """
    Serializer para o modelo Lawyer.

    Atributos:
        company: Usado para listar as empresas que o advogado trabalha.

    Métodos:
        Não há métodos neste serializer.

    Campos:
        name: Nome do advogado.
        username: Username mostrado no perfil do advogado.
        bio: Descrição da biografia do advogado
        company: Empresa na qual o advogado está associado.
    """

    company = CompanySerializer()

    class Meta:
        model = Lawyer
        fields = ('name', 'username', 'bio', 'company')
