from django.shortcuts import render
from property.views import hot_properties
from property.models import Property
# Create your views here.
def index(request, *args, **kwargs):
    context = {
        'carousel_property_list': hot_properties(4),
        'hot_property_list': hot_properties(4),
        'recommended_property_list': hot_properties(4)
    }
    return render(request, 'index.html', context)

def blog(request, *args, **kwargs):
    return render(request, 'blog.html')
