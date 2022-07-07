import imp
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pipes import Template
from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, UpdateView, DetailView
from django.core.paginator import Paginator
from classbased.models import Laptops
from .forms import LaptopRegistration
from django.urls import reverse_lazy
# Create your views here.

@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
class LaptopListView(ListView):
    model = Laptops
    template_name='classbased/laptop-list.html'
    context_object_name='laptops'

    # def get_context_data(self,*args,**kwargs):
    #      laptops=self.get_queryset()
    #      paginator =Paginator(laptops,2)
    #      page_number =self.request.get('page')
    #      page_obj=paginator.get_page(page_number)
    #      context={'laptops':page_obj}
    #      return context
@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
class LaptopCreateView(CreateView):
    form_class = LaptopRegistration
    template_name = 'classbased/Laptop-create.htm'
    success_url =reverse_lazy('Laptop-list')

@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
class LaptopsUpdateView(UpdateView):
    model= Laptops
    template_name ='classbased/laptop-update.htm'
    context_object_name = 'laptop'
    fields =('manufacturer','name','ram','gpu','cpu','price') 
    success_url =reverse_lazy('Laptop-list')

@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
class LaptopDeleteViews(DeleteView):
    model= Laptops
    template_name='classbased/Laptop-delete.htm'
    success_url= reverse_lazy('Laptop-list')

