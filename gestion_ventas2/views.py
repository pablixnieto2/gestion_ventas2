# gestion_ventas2/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def test_view(request):
    return render(request, 'test.html')
