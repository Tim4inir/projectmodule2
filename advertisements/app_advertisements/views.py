from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementsForm

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')

def register(request):
    return render(request, 'register.html')

def advertisement_post(request):
    form = AdvertisementsForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

