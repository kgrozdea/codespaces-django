from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import adicionaAviso
from .models import Aviso


def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

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
