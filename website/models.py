from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier for 
    authentication instead of username.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

# Create your models here.
class User(AbstractUser):
    telefone = models.CharField(max_length=11)
    data_nasc = models.DateField(null = True)
    dados_pix = models.CharField(max_length=100, null = True)
    cpf = models.CharField(max_length=11, null = True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    email = models.EmailField(("email address"), unique=True)
    username=None

    foto_cadastro=models.ImageField(upload_to="Foto_cadastro", null=True)
    doc_pdf=models.FileField(upload_to="Documentos", null=True)

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    def is_adm(self):
        return self.groups.filter(name="adm").exists()

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome        
