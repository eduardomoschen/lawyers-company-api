from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from lawyers.models import Lawyer
from lawyers.serializers import LawyerSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class LawyerList(APIView):
    """
    Representação da API para gerenciar as contas dos advogados.

    Atributos:
        perimssion_classes: Garante a autenticação para operações concedidas
        apenas à usuários que estão logados.

    Métodos:
        get: Retorna todas as contas de advogados registradas.
        post: Cria uma nova conta de advogado. 

    Endpoint Base:
        /api/v1/lawyers/
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Método HTTP GET para listar todas as contas registradas.

        Parâmetros:
            request: O objeto da solicitação HTTP.

        Exemplos de Uso:
            GET /api/v1/lawyers/
            GET /api/v1/lawyers?query=

        Exemplo de Resposta JSON:
            {
                "id": 2,
                "company": 4,
                "name": "Jon Doe",
                "username": "jdoe",
                "bio": "I'm a lawyer specializing in labor rights in the
                programming field."
            }

        Retorna:
            Response: Uma resposta HTTP contendo uma lista de contas em formato
            JSON.
        """

        query = request.GET.get('query')

        if query is None:
            query = ''

        lawyers = Lawyer.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query)
        )

        if not lawyers.exists():
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = LawyerSerializer(lawyers, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Método HTTP POST para criar uma nova conta. Envia os dados da nova
        conta em formato JSON no corpo da solicitação.

        Parâmetros:
            request: O objeto da solicitação HTTP.

        Exemplos de Uso:
            POST /api/v1/lawyers/

        Exemplo de Request Body:
            {
                "company": 4,
                "name": "Jon Doe",
                "username": "jdoe",
                "bio": "I'm a lawyer specializing in labor rights in the
                programming field."
            }

        Retorna:
            Response: Em caso de sucesso, uma resposta HTTP com status 201
            Created como confirmação, junto com os dados da nova conta. Caso
            contrário, retorna uma resposta HTTP com status 400 Bad Request
            indicando que houve falha na criação da conta.
        """

        serializer = LawyerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LawyerDetail(APIView):
    """
    Representação da API que lida com operações detalhadas sobre a conta
    específica do advogado.

    Atributos:
        permission_classes: Garante a autenticação para operações concedidas
        apenas à usuários que estão logados.

    Métodos:
        get_lawyer: Obtém a conta específica com base no username.
        get: Retorna a lista com os detalhes da conta pesquisada.
        put: Atualiza os dados da conta do advogado.
        delete: Deleta a conta do advogado.

    Endpoint Base:
        /api/v1/lawyers/username
    """

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_lawyer(self, username):
        """
        Método auxiliar para obter uma conta com base no username.

        Parâmetros:
            username: O username da conta a ser obtida.

        Retorna:
            lawyer: A conta do advogado encontrada.
        """

        lawyer = get_object_or_404(
            Lawyer.objects.all(),
            username=username
        )

        return lawyer

    def get(self, request, username):
        """
        Método HTTP GET para obter detahes de uma conta específica.

        Parâmetros:
            request: O objeto da solicitação HTTP.
            username: O username da conta a ser encontrada.

        Retorna:
            Response: Uma resposta HTTP contendo os detalhes da conta em
            formato JSON.
        """

        lawyer = self.get_lawyer(username)
        serializer = LawyerSerializer(lawyer, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        """
        Método HTTP PUT para atualizar os dados de uma conta específica.

        Parâmetros:
            request: O objeto da solicitação HTTP.
            username: O username da conta a ser atualizada.

        Retorna:
            Response: Uma resposta HTTP contendo os detalhes da conta 
            atualizada como confirmação. Caso contrário, uma resposta HTTP com
            status 400 Bad Request.
        """

        lawyer = self.get_lawyer(username)

        serializer = LawyerSerializer(lawyer, data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        """
        Método HTTP DELETE para excluir uma conta específica.

        Parâmetros:
            request: O objeto da solicitação HTTP.
            username: O username da conta a ser excluída.

        Retorna:
            Response: Uma resposta HTTP com status 204 No Content como
            confirmação.
        """

        lawyer = self.get_lawyer(username)
        lawyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
