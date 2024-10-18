from django import forms
from .models import User
class DateInput(forms.DateInput):
    input_type="date"


class UserForm (forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User
        fields = [
            "password",
            "first_name",
            "last_name",
            "email",
            "telefone",
            "data_nasc",
            "dados_pix",
            "cpf",
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