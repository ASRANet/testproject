from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def venue(request):
    return render(request, 'venue.html')


def accomodation(request):
    return render(request, 'accomodation.html')


def contactus(request):
    return render(request, 'contactUs.html')


def travel(request):
    return render(request, 'travel.html')


def cookies(request):
    return render(request, 'cookies.html')
