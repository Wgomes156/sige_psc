from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.loginview),
    path("cliente", views.create_user, name="criar-usuario"),
    path("cadastros", views.create_user_adm),

]

