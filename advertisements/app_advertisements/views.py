from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementsForm
from django.urls import reverse

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisement/index.html', context)


def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')

def register(request):
    return render(request, 'app_auth/register.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            # advertisement = Advertisement(**form.cleaned_data)
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)

    else:
        form = AdvertisementsForm()
    context = {'form': form}
    return render(request, 'app_advertisement/advertisement-post.html', context)

def profile(request):
    return render(request, 'app_auth/profile.html')

def login(request):
    return render(request, 'app_auth/login.html')

