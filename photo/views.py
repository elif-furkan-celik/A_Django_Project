from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Photos
from .forms import UpdateForm0, UpdateForm1, UpdateForm2, UpdateForm3, UpdateForm4
from django.contrib import messages
import random
from django.urls import reverse
import random


def update(request, id):
    photo = get_object_or_404(Photos, id=id)
    
    if photo.using_count == 0:
        form = UpdateForm0(request.POST or None, request.FILES or None, instance=photo)
    elif photo.using_count == 1:
        form = UpdateForm1(request.POST or None, request.FILES or None, instance=photo)
    elif photo.using_count == 2:
        form = UpdateForm2(request.POST or None, request.FILES or None, instance=photo)
    elif photo.using_count == 3:
        form = UpdateForm3(request.POST or None, request.FILES or None, instance=photo)
    elif photo.using_count == 4:
        form = UpdateForm4(request.POST or None, request.FILES or None, instance=photo)
    
    phots = Photos.objects.all()
    photos = list(phots)
    random.shuffle(photos)
    photos = photos[:50]

    if form.is_valid():

        photo.using_count = photo.using_count + 1
        photo.save()
        form.save()
        return HttpResponseRedirect("/photo/update/{}".format(photos[0].id))
    context = {
        'form' : form,
        'photo': photo,
        'photos': photos,
    }
    return render(request,
                'photo/template.html', 
                context=context)

def update_1(request):
    return HttpResponseRedirect("/photo/update/{}".format(random.randint(1, 6984)))