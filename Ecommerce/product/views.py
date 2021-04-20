from django.shortcuts import render,redirect
from product.models import Product, Tag
from product.forms import ProductForm, TagForm
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class ProductListView(ListView):
    model = Product

    def get_query_set(self):
        return product.objects.all.order_by('name')

class ProductDetailView(DetailView):
    model = Product

class CreateProductView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'product/product_detail.html'

    form_class = ProductForm
    second_form_class = TagForm

    model = Product
   

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'product/product_detail.html'

    form_class = ProductForm

    model = Product

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product

    success_url = reverse_lazy('product_list') 


def logout_view(request):
    logout(request)
    return redirect('product_list')