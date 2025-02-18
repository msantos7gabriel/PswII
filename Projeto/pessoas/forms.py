from django import forms


class PessoaForm(forms.Form):
    nome = forms.CharField(max_length=100)
    idade = forms.IntegerField(max_value=110)
