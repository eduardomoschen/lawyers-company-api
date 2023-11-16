from rest_framework.serializers import ModelSerializer, SerializerMethodField
from company.models import Company


class CompanySerializer(ModelSerializer):
    """
    Serializer para o modelo Company.

    Atributos:
        employee_count: Campo calculado que representa a quantidade de
        advogados associados à empresa.

    Métodos:
        get_employee_count: Método que retorna a quantidade de advogados
        associados à empresa.

    Campos:
        Todos os campos do modelo Company
    """

    employee_count = SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self, object):
        """
        Obtém o número de advogados associados à empresa.

        Atributos:
            object: Instância do objeto company.

        Retorna:
            count: O número de advogados associados à empresa.
        """

        count = object.lawyer_set.count()
        return count
