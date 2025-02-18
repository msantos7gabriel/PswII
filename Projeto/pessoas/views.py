from django.shortcuts import render, redirect
from .models import Pessoas
from .forms import PessoaForm
from django.http import HttpResponse


def index(request):
    pessoas = Pessoas.objects.all()
    context = {'pessoas': pessoas}
    return render(request, 'pessoas/index.html', context)


def detalhe(request, pk):
    pessoa = Pessoas.objects.get(id=pk)
    context = {'pessoa': pessoa}
    return render(request, 'pessoas/detalhe.html', context)


def add(request):
    form = PessoaForm()
    context = {'form': form}

    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-pessoa')

    return render(request, 'pessoas/form.html', context)


def remove(request, pk):
    pessoa = Pessoas.objects.get(id=pk)
    pessoa.delete()
    return redirect('index-pessoa')


def update(request, pk):
    pessoa = Pessoas.objects.get(id=pk)
    form = PessoaForm(instance=pessoa)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('index-pessoa')

    context = {'form': form}
    return render(request, 'pessoas/form.html', context)
