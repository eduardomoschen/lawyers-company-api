from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from lawyers.models import Lawyer
from lawyers.serializers import LawyerSerializer


class LawyerList(APIView):
    def get(self, request):
        query = request.GET.get('query')

        if query == None:
            query = ''

        laywers = Lawyer.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query)
        )

        if not laywers.exists():
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = LawyerSerializer(laywers, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = LawyerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LawyerDetail(APIView):
    def get_lawyer(self, username):
        lawyer = get_object_or_404(
            Lawyer.objects.all(),
            username=username
        )

        return lawyer

    def get(self, request, username):
        lawyer = self.get_lawyer(username)
        serializer = LawyerSerializer(lawyer, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        lawyer = self.get_lawyer(username)

        serializer = LawyerSerializer(lawyer, data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        lawyer = self.get_lawyer(username)
        lawyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
