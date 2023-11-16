from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.urls import path
from company import views

urlpatterns = [
    path(
        'companies/',
        views.CompanyList.as_view(),
        name='company-list-view'
    ),

    path(
        'companies/<str:name>',
        views.CompanyDetail.as_view(),
        name='company-detail-view'
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
