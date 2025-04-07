from django.urls import path, include
from website import views
from django.conf.urls.static import static
#Caminhos do menu novo
urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.loginview),
    path("cliente", views.create_user, name="criar-usuario"),
    path("cadastros", views.create_user_adm),
    path("sobre", views.about),
    path("aviso", views.aviso),
    path("contato", views.contato),
    path("accounts/", include("django.contrib.auth.urls"))
    # path("foto_usuario", views.foto_perfil),
    ] + static("Foto_cadastro", document_root="Foto_cadastro") + static ("Documentos", document_root="Documentos")



