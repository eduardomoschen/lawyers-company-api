from rest_framework.serializers import ModelSerializer, SerializerMethodField
from company.models import Company
from lawyers.models import Lawyer


class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self, object):
        count = object.lawyer_set.count()
        return count
