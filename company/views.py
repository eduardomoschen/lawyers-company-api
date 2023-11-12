from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from company.models import Company
from company.serializers import CompanySerializer


class CompanyList(APIView):
    def get(self, request):
        companies = Company.objects.all()

        if not companies.exists():
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)
