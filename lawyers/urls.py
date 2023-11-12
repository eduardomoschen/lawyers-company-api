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
    )
]
