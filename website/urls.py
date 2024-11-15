from django.urls import path
from website import views
from django.conf.urls.static import static
#Caminhos do menu novo
urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.loginview),
    path("cliente", views.create_user, name="criar-usuario"),
    path("cadastros", views.create_user_adm),
    
] + static("Foto_cadastro", document_root="Foto_cadastro")



