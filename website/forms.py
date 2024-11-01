from django import forms
from .models import User
class DateInput(forms.DateInput):
    input_type="date"

class UserForm (forms.ModelForm):
    class Meta: 
        
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "telefone",
            "data_nasc",
            "dados_pix",
            "cpf",
            "foto_cadastro"
        ]
        widgets={
            "data_nasc": DateInput()
        }

class CreateUserForm (forms.ModelForm):
    class Meta: 
        model = User
        fields = [
            "email",
                        ]