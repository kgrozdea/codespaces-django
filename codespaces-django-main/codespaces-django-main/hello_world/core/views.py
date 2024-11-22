from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import adicionaAviso
from .models import Aviso


def index(request):
    aviso = Aviso.objects.get(pk=1)
    try: # tenta encontrar referência no banco
        aviso = Aviso.objects.get(pk=1)
    except: # se der erro, coloca variável como None
        aviso = None
    return render(request, "index.html", {'aviso':aviso})

def create_aviso(request):
    if request.method == 'POST':
        form = AvisoForm(request.POST)
        if form.is_valid():
            aviso = form.save(commit=False)  # Create an instance without saving it to the database
            aviso.user = request.user        # Set the user to the logged-in user
            aviso.date_posted = timezone.now()  # Set the date to today's date
            aviso.save()                     # Save the instance to the database
            return redirect('some-view-name')  # Redirect to a success page
    else:
        form = AvisoForm()

    return render(request, 'create_aviso.html', {'form': form})

def adicionar_aviso(request):
 form = AvisoForm()
    if request.method == 'POST' and request.POST:
        form = AvisoForm(request.POST)
        if formulario.is_valid():
            form.save()
            return redirect("/index")

    return render(request,'create_aviso.html',{'form': form})

def editar_referencia(request, id):
    aviso = Aviso.objects.get(pk=id)
    form = AvisoForm(instance=referencia)
    if request.method == 'POST' and request.POST:
        form = AvisoForm(request.POST, instance=aviso)
        if form.is_valid():
             form.save()
            return redirect("/index")

    return render(request,'edit_aviso.html',{'form': form})

def remove_aviso(request, id):
 aviso = Aviso.objects.get(pk=id)
 if request.method == 'POST' and request.POST:
    referencia.delete()
    return redirect("/index")

 return render(request,'remove_aviso.html',{'aviso': aviso})





