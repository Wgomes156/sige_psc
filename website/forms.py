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
            "tipo_pix",
            "dados_pix",
            "cpf",
            "foto_cadastro",
            "doc_pdf"
        ]
        widgets={
            "data_nasc": DateInput(),
            'tipo_pix': forms.Select(attrs={'id': 'tipo-pix', 'class': 'form-label'}),
            'dados_pix': forms.TextInput(attrs={'id': 'dados-pix', 'class': 'form-label'}),
        }
    # data_nasc = forms.DateField(
    #     required=True,
    #     input_formats=["%d/%m/%Y", "%Y-%m-%d"],
    #     widget=DateInput()
    # )

class CreateUserForm (forms.ModelForm):
    class Meta: 
        model = User
        fields = ["email"]