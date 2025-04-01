from django.forms import ModelForm
from .models import Pessoas


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoas
        fields = '__all__'
