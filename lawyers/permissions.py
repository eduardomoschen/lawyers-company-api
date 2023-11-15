from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Classe de permissão personalizada para verificar se o usuário autenticado
    é o proprietário do perfil.

    Atributos:
        Não há atributos nesta classe.

    Métodos:
        has_object_permission: Verifica se o usuário autenticado é o
        proprietário do perfil.
    """

    def has_object_permission(self, request, view, obj):
        """
        Verifica se o usuário autenticado é o proprietário do objeto fornecido.

        Parâmetros:
            request: O objeto da solicitação HTTP.
            view: A view que está sendo acessada.
            obj: O objeto específico que está sendo acessado.

        Retorna:
            bool: True se o usuário for o proprietário do perfil, False caso
            contrário.
        """

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.username == request.user.username
