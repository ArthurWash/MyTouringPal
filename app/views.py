from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import BookAShow, BookAShowForm

# def index(request):
#    return HttpResponse("Sup B")

def welcome(request):
    show_details = BookAShow.objects.all()
    context = {'message': "Coming soon B)"}
    return render(request, 'app/welcome.html', context)

def thank_you(request):
    booking_details = BookAShow.objects.all()
    context = {'message': "Thank you for your request! We will get back to you ASAP :)"}
    return render(request, 'app/ThankYou.html', context)


def book(request):
    if request.method == 'POST':
        form = BookAShowForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('thank_you'))
    else:
        form = BookAShowForm()

    return render(request, 'app/Book.html', {'form': form})

def ajax_demo(request):
    data = {
        "Band name": "Faulty Parachute",
        "Genre": "Pop Punk",
        "Latest Release": "Fake It (Single)",
    }
    return JsonResponse(data)