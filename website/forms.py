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
            "telefone",
            "data_nasc",
            "dados_pix",
            "cpf",
            "foto_cadastro",
            "doc_pdf"
        ]
        widgets={
            'first_name': forms.TextInput(attrs={'id': 'first_name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'id': 'last_name', 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'id': 'telefone', 'class': 'form-control mask-telefone', 'placeholder': '(00) 00000-0000'}),
            "data_nasc": DateInput(),
            'dados_pix': forms.TextInput(attrs={'id': 'dados-pix', 'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'id': 'cpf', 'class': 'form-control mask-cpf', 'placeholder': '000.000.000-00'}),
        }

class CreateUserForm (forms.ModelForm):
    class Meta: 
        model = User
        fields = ["email"]