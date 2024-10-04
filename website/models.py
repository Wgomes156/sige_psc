from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    telefone = models.CharField(max_length=100,default="0")
    data_nasc = models.DateField(null = True)
    dados_pix = models.CharField(max_length=100, null = True)
    cpf = models.CharField(max_length=100, null = True)
