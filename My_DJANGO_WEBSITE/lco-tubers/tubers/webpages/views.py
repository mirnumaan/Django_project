from django.shortcuts import render
from .models import Slider,Group
from youtubers.models import Youtuber 


def home(request) :
    sliders = Slider.objects.all()
    groups= Group.objects.all()
    featured_youtubers=Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers=Youtuber.objects.order_by('-created_date')
    data ={
        'sliders':sliders,
        'groups':groups,
        'featured_youtubers':featured_youtubers,
        'all_tubers':all_tubers
    }

    return render(request,'webpages/home.html',data)

def about(request):
    return render(request,'webpages/about.html')

def contact(request):
    return render(request,'webpages/contact.html')

def services(request):
    return render(request,'webpages/services.html')
