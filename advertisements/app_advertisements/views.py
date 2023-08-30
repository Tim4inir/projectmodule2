from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementsForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements,
               'title': title}
    return render(request, 'app_advertisement/index.html', context)


def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')

def register(request):
    return render(request, 'app_auth/register.html')



@login_required(login_url=reverse_lazy('profile'))
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







