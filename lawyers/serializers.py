from rest_framework.serializers import ModelSerializer
from lawyers.models import Lawyer
from company.serializers import CompanySerializer


class LawyerSerializer(ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Lawyer
        fields = ('username', 'bio', 'company')
