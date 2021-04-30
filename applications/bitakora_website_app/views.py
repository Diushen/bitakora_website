from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect

# Create your views here.

def homeView(request):
    context = {}
    return render(request, 'home.tmp.html', context)

def redirectHome(request):
    return redirect('home/')