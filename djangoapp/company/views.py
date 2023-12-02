from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from company.models import Company
from company.serializers import CompanySerializer


class CompanyList(APIView):
    """
    Representação da API para gerenciar as contas das empresas.

    Atributos:
        permission_classes: Garante a autenticação para operações concedidas
        apenas à usuários que estão logados.

    Métodos:
        get: Retorna todas as empresas registradas.
        post: Cria uma nova empresa.

    Endpoint Base:
        /api/v1/companies/
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Método HTTP GET para listar todas as empresas registradas,

        Parâmetros:
            request: O objeto da solicitação HTTP.

        Exemplo de Uso:
            GET /api/v1/companies/

        Exemplo de Resposta JSON:


        Retorna:
            Response: Uma resposta HTTP contendo uma lista de empresas em
            formato JSON.
        """

        companies = Company.objects.all()

        if not companies.exists():
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        Método HTTP POST para criar uma nova empresa. Envia os dados da nova
        empresa em formato JSON no corpo da solicitação. Neste método apenas
        usuários da área administrativa possuem autorização.

        Parâmetros:
            request: O objeto da solicitação HTTP.

        Exemplos de Uso:
            POST /api/v1/companies/

        Exemplo de Request Body:


        Retorna:
            Response: Em caso de sucesso, uma resposta HTTP com status 201
            Created como confirmação, junto com os dados da nova conta. Caso
            contrário, retorna uma resposta HTTP com status 400 Bad Request
            indicando que houve falha na criação da conta. 
        """

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
    """
    Representação da API que lida com operações detalhadas sobre uma empresa
    específica.

    Atributos:
        permission_classes: Garante a autenticação para operações concedidadas
        apenas à usuários que estão logados.

    Métodos:
        get_company: Obtém uma empresa específica com base em seu nome.
        get: Retorna alista com os detalhes da empresa pesquisada.
        put: Atualiza os dados da empresa.
        delete: Deleta a empresa.

    Endpoint Base:
        /api/v1/companies/name
    """

    permission_classes = [IsAuthenticated]

    def get_company(self, name):
        """
        Método auxiliar pra obter uma empresa com base no nome.

        Parâmetros:
            name: O nome da empresa a ser obtida.

        Retorna:
            company: A empresa encontrada.
        """

        company = get_object_or_404(
            Company.objects.all(),
            name=name
        )

        return company

    def get(self, request, name):
        """
        Método HTTP GET para obter detalhes de uma empresa específica.

        Parâmetros:
            request: O objeto da solicitação HTTP.
            name: O nome da empresa a ser listada.

        Retorna:
            Response: Uma resposta HTTP contendo os detalhes da empresa em
            formato JSON.
        """

        company = self.get_company(name)
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)

    def put(self, request, name):
        """
        Método HTTP PUT para atualizar os dados de uma empresa específica. Este
        método é destinado apenas a usuários adminstrativos.

        Parâmetros:
            request: O objeto da solicitação HTTP.
            nome: O nome da empresa a ser atualizada.

        Retorna:
            Response: Uma resposta HTTP contendo os detalhes da empresa 
            atualizada como confirmação. Caso contrário, uma resposta HTTP com
            status 400 Bad Request
        """

        if not request.user.is_superuser:
            raise PermissionDenied(
                "You do not have permission to perform this action."
            )

        company = self.get_company(name)

        serializer = CompanySerializer(company, data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        """
        Método HTTP DELETE para excluir uma empresa específica. Este método é
        destinado apenas a usuários adminstrativos.


        Parâmetros:
            request: O objeto da solicitação HTTP.
            nome: O nome da empresa a ser excluída.

        Retorna:
            Response: Uma resposta HTTP com status 204 No Content como
            confirmação.
        """

        if not request.user.is_superuser:
            raise PermissionDenied(
                "You do not have permission to perform this action."
            )

        company = self.get_company(name)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
