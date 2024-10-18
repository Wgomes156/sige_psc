from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.loginview),
    path("criar-usuario", views.create_user),
    path("criarusuario-adm", views.create_user_adm),
]

