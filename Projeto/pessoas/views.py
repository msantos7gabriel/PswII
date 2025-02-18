from django.shortcuts import render, redirect
from .models import Pessoas
from .forms import PessoaForm
from django.http import HttpResponse


def index(request):
    pessoas = Pessoas.objects.all()
    context = {'pessoas': pessoas}
    return render(request, 'pessoas/index.html', context)


def add(request):
    form = PessoaForm()
    context = {'form': form}

    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-pessoa')

    return render(request, 'pessoas/add.html', context)


def remove(request):
    return HttpResponse('Remover pessoa!')


def update(request):
    return HttpResponse('Atualizar Pessoas !')
