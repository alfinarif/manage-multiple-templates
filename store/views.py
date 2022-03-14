import os
from datetime import time, timedelta

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView


# import models
from store.models import (
    Category, 
    Product, 
    Variations, 
    Banner, 
    SmallBanner,
    AdsBanner,
    Brand,
    PopupOffer
    )

# import forms
from store.forms import (
    BannerCreationForm, 
    SmallBannerCreationForm, 
    AdsBannerCreationForm, 
    CategoryCreationForm, 
    ProductCreationForm, 
    BrandCreationForm,
    VariationsCreationForm
    )



# this product show on dashboard
class ProductList(TemplateView):
    def get(self, request, *args, **kwargs):
        
        products = Product.objects.all().order_by('-id')
    
        context = {
            "products": products
        }

        # check if product_list.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_list.html")):
            return render(request, 'store/data_list.html', context)
        else:
            # creating new product_list.html file with docs data
            with open("templates/store/data_list.html", "w") as f:
                docs = '{%extends "dashboard/base.html"%}{%block body%}{%include "dashboard/sidebar.html"%}<header class="mb-3"><a href="#" class="burger-btn d-block d-xl-none"><i class="bi bi-justify fs-3"></i></a></header><div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>All product list</h3><p class="text-subtitle text-muted">For user to check they list</p></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">DataTable</li></ol></nav></div></div></div>{%if products%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_product" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Old Price</th><th>Stock Status</th><th>Action</th></tr></thead><tbody>{%for product in products%}<tr><td>{{product.id}}</td><td>{{product.name}}</td><td>{{product.category}}</td><td>{{product.price}}</td><td>{{product.old_price}}</td><td>{{product.is_stock}}</td><td><a href="{{ page.get_page_url }}"><span class="badge bg-info">View</span></a></td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif categories%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_category" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Parents</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for category in categories%}<tr><td>{{category.id}}</td><td>{{category.parent}}</td><td>{{category.name}}</td><td>{{category.image}}</td><td>{{category.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif brands%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_brand" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for brand in brands%}<tr><td>{{brand.id}}</td><td>{{brand.name}}</td><td>{{brand.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif variations%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_variation" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Variations</th><th>Names</th><th>Products</th><th>Prices</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for variation in variations%}<tr><td>{{variation.id}}</td><td>{{variation.variation}}</td><td>{{variation.name}}</td><td>{{variation.product}}</td><td>{{variation.price}}</td><td>{{variation.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif banners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_main_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in banners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif smallbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_small_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in smallbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif adsbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_ads_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in adsbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%endif%}</div>{%endblock body%}'
                f.write(docs)   
            return render(request, 'store/data_list.html', context)

    def post(self, request, *args, **kwargs):
        pass


# variation show on dashboard
class VariationList(TemplateView):
    def get(self, request, *args, **kwargs):
        variations = Variations.objects.all().order_by('-id')
        context = {
            "variations": variations
        }
        
        # check if product_list.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_list.html")):
            return render(request, 'store/data_list.html', context)
        else:
            # creating new product_list.html file with docs data
            with open("templates/store/data_list.html", "w") as f:
                docs = '{%extends "dashboard/base.html"%}{%block body%}{%include "dashboard/sidebar.html"%}<header class="mb-3"><a href="#" class="burger-btn d-block d-xl-none"><i class="bi bi-justify fs-3"></i></a></header><div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>All product list</h3><p class="text-subtitle text-muted">For user to check they list</p></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">DataTable</li></ol></nav></div></div></div>{%if products%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_product" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Old Price</th><th>Stock Status</th><th>Action</th></tr></thead><tbody>{%for product in products%}<tr><td>{{product.id}}</td><td>{{product.name}}</td><td>{{product.category}}</td><td>{{product.price}}</td><td>{{product.old_price}}</td><td>{{product.is_stock}}</td><td><a href="{{ page.get_page_url }}"><span class="badge bg-info">View</span></a></td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif categories%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_category" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Parents</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for category in categories%}<tr><td>{{category.id}}</td><td>{{category.parent}}</td><td>{{category.name}}</td><td>{{category.image}}</td><td>{{category.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif brands%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_brand" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for brand in brands%}<tr><td>{{brand.id}}</td><td>{{brand.name}}</td><td>{{brand.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif variations%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_variation" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Variations</th><th>Names</th><th>Products</th><th>Prices</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for variation in variations%}<tr><td>{{variation.id}}</td><td>{{variation.variation}}</td><td>{{variation.name}}</td><td>{{variation.product}}</td><td>{{variation.price}}</td><td>{{variation.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif banners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_main_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in banners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif smallbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_small_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in smallbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif adsbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_ads_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in adsbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%endif%}</div>{%endblock body%}'
                f.write(docs)   
            return render(request, 'store/data_list.html', context)

    def post(self, request, *args, **kwargs):
        pass



# categories show on dashboard
class CategoryList(TemplateView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all().order_by('-id')
        context = {
            "categories": categories
        }
        
        # check if product_list.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_list.html")):
            return render(request, 'store/data_list.html', context)
        else:
            # creating new product_list.html file with docs data
            with open("templates/store/data_list.html", "w") as f:
                docs = '{%extends "dashboard/base.html"%}{%block body%}{%include "dashboard/sidebar.html"%}<header class="mb-3"><a href="#" class="burger-btn d-block d-xl-none"><i class="bi bi-justify fs-3"></i></a></header><div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>All product list</h3><p class="text-subtitle text-muted">For user to check they list</p></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">DataTable</li></ol></nav></div></div></div>{%if products%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_product" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Old Price</th><th>Stock Status</th><th>Action</th></tr></thead><tbody>{%for product in products%}<tr><td>{{product.id}}</td><td>{{product.name}}</td><td>{{product.category}}</td><td>{{product.price}}</td><td>{{product.old_price}}</td><td>{{product.is_stock}}</td><td><a href="{{ page.get_page_url }}"><span class="badge bg-info">View</span></a></td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif categories%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_category" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Parents</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for category in categories%}<tr><td>{{category.id}}</td><td>{{category.parent}}</td><td>{{category.name}}</td><td>{{category.image}}</td><td>{{category.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif brands%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_brand" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for brand in brands%}<tr><td>{{brand.id}}</td><td>{{brand.name}}</td><td>{{brand.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif variations%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_variation" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Variations</th><th>Names</th><th>Products</th><th>Prices</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for variation in variations%}<tr><td>{{variation.id}}</td><td>{{variation.variation}}</td><td>{{variation.name}}</td><td>{{variation.product}}</td><td>{{variation.price}}</td><td>{{variation.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif banners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_main_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in banners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif smallbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_small_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in smallbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif adsbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_ads_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in adsbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%endif%}</div>{%endblock body%}'
                f.write(docs)   
            return render(request, 'store/data_list.html', context)

    def post(self, request, *args, **kwargs):
        pass


# Brand show on dashboard
class BrandList(TemplateView):
    def get(self, request, *args, **kwargs):
        brands = Brand.objects.all().order_by('-id')
        context = {
            "brands": brands
        }
        
        # check if product_list.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_list.html")):
            return render(request, 'store/data_list.html', context)
        else:
            # creating new product_list.html file with docs data
            with open("templates/store/data_list.html", "w") as f:
                docs = '{%extends "dashboard/base.html"%}{%block body%}{%include "dashboard/sidebar.html"%}<header class="mb-3"><a href="#" class="burger-btn d-block d-xl-none"><i class="bi bi-justify fs-3"></i></a></header><div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>All product list</h3><p class="text-subtitle text-muted">For user to check they list</p></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">DataTable</li></ol></nav></div></div></div>{%if products%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_product" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Old Price</th><th>Stock Status</th><th>Action</th></tr></thead><tbody>{%for product in products%}<tr><td>{{product.id}}</td><td>{{product.name}}</td><td>{{product.category}}</td><td>{{product.price}}</td><td>{{product.old_price}}</td><td>{{product.is_stock}}</td><td><a href="{{ page.get_page_url }}"><span class="badge bg-info">View</span></a></td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif categories%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_category" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Parents</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for category in categories%}<tr><td>{{category.id}}</td><td>{{category.parent}}</td><td>{{category.name}}</td><td>{{category.image}}</td><td>{{category.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif brands%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_brand" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for brand in brands%}<tr><td>{{brand.id}}</td><td>{{brand.name}}</td><td>{{brand.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif variations%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_variation" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Variations</th><th>Names</th><th>Products</th><th>Prices</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for variation in variations%}<tr><td>{{variation.id}}</td><td>{{variation.variation}}</td><td>{{variation.name}}</td><td>{{variation.product}}</td><td>{{variation.price}}</td><td>{{variation.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif banners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_main_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in banners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif smallbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_small_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in smallbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif adsbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_ads_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in adsbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%endif%}</div>{%endblock body%}'
                f.write(docs)   
            return render(request, 'store/data_list.html', context)

    def post(self, request, *args, **kwargs):
        pass


# Banner show on dashboard
class BannerList(TemplateView):
    def get(self, request, *args, **kwargs):
        banners = Banner.objects.all().order_by('-id')
        context = {
            "banners": banners
        }
        
        # check if product_list.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_list.html")):
            return render(request, 'store/data_list.html', context)
        else:
            # creating new product_list.html file with docs data
            with open("templates/store/data_list.html", "w") as f:
                docs = '{%extends "dashboard/base.html"%}{%block body%}{%include "dashboard/sidebar.html"%}<header class="mb-3"><a href="#" class="burger-btn d-block d-xl-none"><i class="bi bi-justify fs-3"></i></a></header><div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>All product list</h3><p class="text-subtitle text-muted">For user to check they list</p></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">DataTable</li></ol></nav></div></div></div>{%if products%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_product" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Old Price</th><th>Stock Status</th><th>Action</th></tr></thead><tbody>{%for product in products%}<tr><td>{{product.id}}</td><td>{{product.name}}</td><td>{{product.category}}</td><td>{{product.price}}</td><td>{{product.old_price}}</td><td>{{product.is_stock}}</td><td><a href="{{ page.get_page_url }}"><span class="badge bg-info">View</span></a></td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif categories%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_category" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Parents</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for category in categories%}<tr><td>{{category.id}}</td><td>{{category.parent}}</td><td>{{category.name}}</td><td>{{category.image}}</td><td>{{category.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif brands%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_brand" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for brand in brands%}<tr><td>{{brand.id}}</td><td>{{brand.name}}</td><td>{{brand.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif variations%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_variation" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Variations</th><th>Names</th><th>Products</th><th>Prices</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for variation in variations%}<tr><td>{{variation.id}}</td><td>{{variation.variation}}</td><td>{{variation.name}}</td><td>{{variation.product}}</td><td>{{variation.price}}</td><td>{{variation.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif banners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_main_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in banners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif smallbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_small_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in smallbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif adsbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_ads_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in adsbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%endif%}</div>{%endblock body%}'
                f.write(docs)   
            return render(request, 'store/data_list.html', context)

    def post(self, request, *args, **kwargs):
        pass


# Small Banner show on dashboard
class SmallBannerList(TemplateView):
    def get(self, request, *args, **kwargs):
        smallbanners = SmallBanner.objects.all().order_by('-id')
        context = {
            "smallbanners": smallbanners
        }
        
        # check if product_list.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_list.html")):
            return render(request, 'store/data_list.html', context)
        else:
            # creating new product_list.html file with docs data
            with open("templates/store/data_list.html", "w") as f:
                docs = '{%extends "dashboard/base.html"%}{%block body%}{%include "dashboard/sidebar.html"%}<header class="mb-3"><a href="#" class="burger-btn d-block d-xl-none"><i class="bi bi-justify fs-3"></i></a></header><div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>All product list</h3><p class="text-subtitle text-muted">For user to check they list</p></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">DataTable</li></ol></nav></div></div></div>{%if products%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_product" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Old Price</th><th>Stock Status</th><th>Action</th></tr></thead><tbody>{%for product in products%}<tr><td>{{product.id}}</td><td>{{product.name}}</td><td>{{product.category}}</td><td>{{product.price}}</td><td>{{product.old_price}}</td><td>{{product.is_stock}}</td><td><a href="{{ page.get_page_url }}"><span class="badge bg-info">View</span></a></td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif categories%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_category" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Parents</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for category in categories%}<tr><td>{{category.id}}</td><td>{{category.parent}}</td><td>{{category.name}}</td><td>{{category.image}}</td><td>{{category.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif brands%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_brand" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for brand in brands%}<tr><td>{{brand.id}}</td><td>{{brand.name}}</td><td>{{brand.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif variations%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_variation" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Variations</th><th>Names</th><th>Products</th><th>Prices</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for variation in variations%}<tr><td>{{variation.id}}</td><td>{{variation.variation}}</td><td>{{variation.name}}</td><td>{{variation.product}}</td><td>{{variation.price}}</td><td>{{variation.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif banners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_main_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in banners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif smallbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_small_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in smallbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif adsbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_ads_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in adsbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%endif%}</div>{%endblock body%}'
                f.write(docs)   
            return render(request, 'store/data_list.html', context)

    def post(self, request, *args, **kwargs):
        pass


# Ads Banner show on dashboard
class AdsBannerList(TemplateView):
    def get(self, request, *args, **kwargs):
        adsbanners = AdsBanner.objects.all().order_by('-id')
        context = {
            "adsbanners": adsbanners
        }
        
        # check if product_list.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_list.html")):
            return render(request, 'store/data_list.html', context)
        else:
            # creating new product_list.html file with docs data
            with open("templates/store/data_list.html", "w") as f:
                docs = '{%extends "dashboard/base.html"%}{%block body%}{%include "dashboard/sidebar.html"%}<header class="mb-3"><a href="#" class="burger-btn d-block d-xl-none"><i class="bi bi-justify fs-3"></i></a></header><div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>All product list</h3><p class="text-subtitle text-muted">For user to check they list</p></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">DataTable</li></ol></nav></div></div></div>{%if products%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_product" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Old Price</th><th>Stock Status</th><th>Action</th></tr></thead><tbody>{%for product in products%}<tr><td>{{product.id}}</td><td>{{product.name}}</td><td>{{product.category}}</td><td>{{product.price}}</td><td>{{product.old_price}}</td><td>{{product.is_stock}}</td><td><a href="{{ page.get_page_url }}"><span class="badge bg-info">View</span></a></td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif categories%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_category" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Parents</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for category in categories%}<tr><td>{{category.id}}</td><td>{{category.parent}}</td><td>{{category.name}}</td><td>{{category.image}}</td><td>{{category.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif brands%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_brand" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Names</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for brand in brands%}<tr><td>{{brand.id}}</td><td>{{brand.name}}</td><td>{{brand.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif variations%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_variation" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Variations</th><th>Names</th><th>Products</th><th>Prices</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for variation in variations%}<tr><td>{{variation.id}}</td><td>{{variation.variation}}</td><td>{{variation.name}}</td><td>{{variation.product}}</td><td>{{variation.price}}</td><td>{{variation.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif banners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_main_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in banners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif smallbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_small_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in smallbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%elif adsbanners%}<section class="section"><div class="card"><div class="card-header"><a href="{% url "store:create_ads_banner" %}"><span class="badge bg-info">Add new</span></a></div><div class="card-body"><table class="table table-striped" id="table1"><thead><tr><th>ID</th><th>Product</th><th>Is Active</th><th>Images</th><th>Created At</th><th>Action</th></tr></thead><tbody>{%for banner in adsbanners%}<tr><td>{{banner.id}}</td><td>{{banner.product}}</td><td>{{banner.is_active}}</td><td>{{banner.image}}</td><td>{{banner.created}}</td><td><span class="badge bg-primary">Edit</span></td></tr>{%endfor%}</tbody></table></div></div></section>{%endif%}</div>{%endblock body%}'
                f.write(docs)   
            return render(request, 'store/data_list.html', context)

    def post(self, request, *args, **kwargs):
        pass


















#===================================== CREATION SECTION ================================
# Creation Class View Start From Here

# product creating from dashboard
class ProductCreationTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = ProductCreationForm()
        context = {
            'form': form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_creation.html")):
            return render(request, 'store/data_creation.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/store/data_creation.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% load crispy_forms_tags %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3 uniForm">{{form|crispy}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'store/data_creation.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            form = ProductCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('store:product_list')
        
        return render(request, 'store/data_creation.html')



# category creating from dashboard
class CategoryCreationTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = CategoryCreationForm()
        context = {
            'form': form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_creation.html")):
            return render(request, 'store/data_creation.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/store/data_creation.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% load crispy_forms_tags %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3 uniForm">{{form|crispy}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'store/data_creation.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            form = CategoryCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('store:category_list')
        
        return render(request, 'store/data_creation.html')


# brand creating from dashboard
class BrandCreationTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = BrandCreationForm()
        context = {
            'form': form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_creation.html")):
            return render(request, 'store/data_creation.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/store/data_creation.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% load crispy_forms_tags %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3 uniForm">{{form|crispy}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'store/data_creation.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            form = BrandCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('store:brand_list')
        
        return render(request, 'store/data_creation.html')


# Variation creating from dashboard
class VariationCreationTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = VariationsCreationForm()
        context = {
            'form': form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_creation.html")):
            return render(request, 'store/data_creation.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/store/data_creation.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% load crispy_forms_tags %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3 uniForm">{{form|crispy}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'store/data_creation.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            form = VariationsCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('store:variation_list')
        
        return render(request, 'store/data_creation.html')




# Main Banner creating from dashboard
class MainBannerCreationTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = BannerCreationForm()
        context = {
            'form': form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_creation.html")):
            return render(request, 'store/data_creation.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/store/data_creation.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% load crispy_forms_tags %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3 uniForm">{{form|crispy}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'store/data_creation.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            form = BannerCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('store:main_banner')
        
        return render(request, 'store/data_creation.html')


# Small Banner creating from dashboard
class SmallBannerCreationTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = SmallBannerCreationForm()
        context = {
            'form': form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_creation.html")):
            return render(request, 'store/data_creation.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/store/data_creation.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% load crispy_forms_tags %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3 uniForm">{{form|crispy}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'store/data_creation.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            form = SmallBannerCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('store:small_banner')
        
        return render(request, 'store/data_creation.html')


# Ads Banner creating from dashboard
class AdsBannerCreationTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = AdsBannerCreationForm()
        context = {
            'form': form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/store/data_creation.html")):
            return render(request, 'store/data_creation.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/store/data_creation.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% load crispy_forms_tags %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3 uniForm">{{form|crispy}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'store/data_creation.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            form = AdsBannerCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('store:ads_banner')
        
        return render(request, 'store/data_creation.html')





#===================================== Object Update SECTION ================================
# UPDATE Class View Start From Here

# product model update class view
class ProductUpdateView(UpdateView):
    template_name = "store/data_creation.html"
    model = Product
    fields = ('__all__')
    context_object_name = 'form'

    def get_success_url(self):
        return reverse("store:product_list")


# Category model update class view
class CategoryUpdateView(UpdateView):
    template_name = "store/data_creation.html"
    model = Category
    fields = ('__all__')
    context_object_name = 'form'

    def get_success_url(self):
        return reverse("store:category_list")


# Variation model update class view
class VariationUpdateView(UpdateView):
    template_name = "store/data_creation.html"
    model = Variations
    fields = ('__all__')
    context_object_name = 'form'

    def get_success_url(self):
        return reverse("store:variation_list")


# Brand model update class view
class BrandUpdateView(UpdateView):
    template_name = "store/data_creation.html"
    model = Brand
    fields = ('__all__')
    context_object_name = 'form'

    def get_success_url(self):
        return reverse("store:brand_list")

# Banner model update class view
class BannerUpdateView(UpdateView):
    template_name = "store/data_creation.html"
    model = Banner
    fields = ('__all__')
    context_object_name = 'form'

    def get_success_url(self):
        return reverse("store:main_banner")


# Small Banner model update class view
class SmallBannerUpdateView(UpdateView):
    template_name = "store/data_creation.html"
    model = SmallBanner
    fields = ('__all__')
    context_object_name = 'form'

    def get_success_url(self):
        return reverse("store:small_banner")


# Ads Banner model update class view
class AdsBannerUpdateView(UpdateView):
    template_name = "store/data_creation.html"
    model = AdsBanner
    fields = ('__all__')
    context_object_name = 'form'

    def get_success_url(self):
        return reverse("store:ads_banner")





#===================================== Object DELETE SECTION ================================
# DELETE Class View Start From Here

# product model update class view
class ProductDeleteView(DeleteView):
    template_name = "store/delete_confirmation.html"
    model = Product

    def get_success_url(self):
        return reverse("store:product_list")


# Category model update class view
class CategoryDeleteView(DeleteView):
    template_name = "store/delete_confirmation.html"
    model = Category

    def get_success_url(self):
        return reverse("store:category_list")


# Variation model update class view
class VariationDeleteView(DeleteView):
    template_name = "store/delete_confirmation.html"
    model = Variations

    def get_success_url(self):
        return reverse("store:variation_list")


# Brand model update class view
class BrandDeleteView(DeleteView):
    template_name = "store/delete_confirmation.html"
    model = Brand

    def get_success_url(self):
        return reverse("store:brand_list")

# Banner model update class view
class BannerDeleteView(DeleteView):
    template_name = "store/delete_confirmation.html"
    model = Banner

    def get_success_url(self):
        return reverse("store:main_banner")


# Small Banner model update class view
class SmallBannerDeleteView(DeleteView):
    template_name = "store/delete_confirmation.html"
    model = SmallBanner

    def get_success_url(self):
        return reverse("store:small_banner")


# Ads Banner model update class view
class AdsBannerDeleteView(DeleteView):
    template_name = "store/delete_confirmation.html"
    model = AdsBanner

    def get_success_url(self):
        return reverse("store:ads_banner")