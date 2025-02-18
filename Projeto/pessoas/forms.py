from django import forms
from .models import Pessoas


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoas
        fields = '__all__'
