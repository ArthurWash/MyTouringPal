from django.http import HttpResponse
from django.shortcuts import render
from .models import BookAShow

# def index(request):
#    return HttpResponse("Sup B")

def welcome(request):
    show_details = BookAShow.objects.all()
    context = {'message': "Coming soon B)"}
    return render(request, 'app/welcome.html', context)