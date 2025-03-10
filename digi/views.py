from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from digi.models import Digidex
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# View de registro de usuários
class RegisterViewCreate(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/cadastro.html'
    success_url = reverse_lazy('digi:login')

# View personalizada de login
class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('digi:home')

# Lista de Digimons com paginação e busca
class DigiList(ListView):
    model = Digidex
    template_name = 'home.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('nome')
        if query:
            queryset = queryset.filter(nome__icontains=query)
        
        orderby = self.request.GET.get('orderby')
        if not orderby:  # Se 'orderby' estiver vazio, usar '-nome' por padrão
            orderby = '-nome'
        
        return queryset.order_by(orderby)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')
        try:
            digimons = paginator.page(page)
        except PageNotAnInteger:
            digimons = paginator.page(1)
        except EmptyPage:
            digimons = paginator.page(paginator.num_pages)

        context['digimons'] = digimons
        context['is_paginated'] = paginator.num_pages > 1
        return context

# CRUD: Criação, atualização, detalhes e exclusão de Digimons
class DigiCreate(CreateView):
    model = Digidex
    fields = '__all__'
    success_url = reverse_lazy('digi:home')
    template_name = 'crud/create.html'

class DigiUpdate(UpdateView):
    model = Digidex
    fields = '__all__'
    success_url = reverse_lazy('digi:home')
    template_name = 'crud/create.html'

class DigiDetail(DetailView):
    model = Digidex
    template_name = 'crud/detail.html'

class DigiDelete(DeleteView):
    model = Digidex
    success_url = reverse_lazy('digi:home')
    template_name = 'crud/delete.html'
