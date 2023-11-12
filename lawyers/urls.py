from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.urls import path
from lawyers import views

urlpatterns = [
    path(
        'lawyers',
        views.LawyerList.as_view(),
        name='lawyrers-list-view'
    ),

    path(
        'lawyers/<str:username>',
        views.LawyerDetail.as_view(),
        name='lawyers-detail-view'
    ),

    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    path(
        'token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
]
