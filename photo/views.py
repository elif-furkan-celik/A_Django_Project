from django.shortcuts import render
from .models import Photos


def index(request):
    
    return render(request,
                'photo/index.html', 
                context={"photo": Photos.objects.all})
