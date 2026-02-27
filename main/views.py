from django.shortcuts import render
from machines.models import *

def index(request):
    data = {
        'title': 'SMART INDUSTRY',
        'values': ['Some', 'hello', 'world'],
        'obj': {
            'machine': 'Hyundai',
            'axis': 5,
            'type': 'CNC'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
