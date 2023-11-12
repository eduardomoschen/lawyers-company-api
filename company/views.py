from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from company.models import Company
from company.serializers import CompanySerializer


class CompanyList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        companies = Company.objects.all()

        if not companies.exists():
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_superuser:
            raise PermissionDenied(
                "You do not have permission to perform this action."
            )

        serializer = CompanySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_company(self, username):
        company = get_object_or_404(
            Company.objects.all(),
            username=username
        )

        return company

    def get(self, request, username):
        company = self.get_company(username)
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        if not request.user.is_superuser:
            raise PermissionDenied(
                "You do not have permission to perform this action."
            )

        company = self.get_company(username)

        serializer = CompanySerializer(company, data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        if not request.user.is_superuser:
            raise PermissionDenied(
                "You do not have permission to perform this action."
            )

        company = self.get_company(username)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
