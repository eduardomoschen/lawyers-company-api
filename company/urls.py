from django.urls import path
from company import views

urlpatterns = [
    path(
        'companies/',
        views.CompanyList.as_view(),
        name='company-list-view'
    )
]
