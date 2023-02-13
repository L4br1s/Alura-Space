from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages



from django.http import HttpResponse


def index(request):
    if not request.user.is_authenticated:
        messages.error(request,"Faça o login para utilizar essa feature")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_Publicada").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,"Faça o login para utilizar essa feature")
        return redirect('login')
    fotografia = Fotografia.objects.order_by("data_Publicada").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografia = fotografia.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/buscar.html', {"cards": fotografia})