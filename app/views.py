from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import BookAShow, BookAShowForm

# def index(request):
#    return HttpResponse("Sup B")

def welcome(request):
    show_details = BookAShow.objects.all()
    context = {'message': "Coming soon B)"}
    return render(request, 'app/welcome.html', context)

def book(request):
    if request.method == 'POST':
        form = BookAShowForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = BookAShowForm()

    return render(request, 'app/Book.html', {'form': form})