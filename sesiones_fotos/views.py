from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SesionFoto
from .forms import SesionFotoForm

class SesionFotoListView(ListView):
    model = SesionFoto
    template_name = 'sesiones_fotos/sesionfoto_list.html'
    context_object_name = 'sesiones_fotos'

class SesionFotoDetailView(DetailView):
    model = SesionFoto
    template_name = 'sesiones_fotos/sesionfoto_detail.html'

class SesionFotoCreateView(CreateView):
    model = SesionFoto
    form_class = SesionFotoForm
    template_name = 'sesiones_fotos/sesionfoto_form.html'

class SesionFotoUpdateView(UpdateView):
    model = SesionFoto
    form_class = SesionFotoForm
    template_name = 'sesiones_fotos/sesionfoto_form.html'

class SesionFotoDeleteView(DeleteView):
    model = SesionFoto
    template_name = 'sesiones_fotos/sesionfoto_confirm_delete.html'
    success_url = '/sesiones_fotos/'
