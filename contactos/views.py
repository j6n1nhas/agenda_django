from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from .models import Contacto


def index(request):
    contactos = Contacto.objects.order_by('-nome').filter(mostrar=True)
    pagina = Paginator(contactos, 10)
    pag = request.GET.get('page')
    contactos = pagina.get_page(pag)
    return render(request, 'contactos/index.html', {'contactos': contactos})


def detalhe(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if not contacto.mostrar:
        raise Http404
    return render(request, 'contactos/detalhe.html', {'contacto': contacto})


def busca(request):
    termo = request.GET.get('termo')
    if termo is None:
        messages.add_message(request, messages.ERROR, 'Campo de busca inválido')
        return redirect('index')
    campos = Concat('nome', Value(' '), 'apelido')
    contactos = Contacto.objects.annotate(nome_completo=campos).filter(Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo))
    pagina = Paginator(contactos, 10)
    pag = request.GET.get('page')
    contactos = pagina.get_page(pag)
    return render(request, 'contactos/index.html', {'contactos': contactos})
