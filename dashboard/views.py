import os
import random
from django.db.models import fields

from django.shortcuts import render
from django.urls import reverse

from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from django.http import HttpResponseRedirect
from dashboard import models

from order.models import Order

from dashboard.models import FavIcon, PageTitle, Pages, SelectTemplate
from dashboard.forms import (
    PagesForm, 
    PageTitleForm, 
    FavIconForm, 
    MainIconForm
    )

from store.models import Banner, SmallBanner, AdsBanner, Category, Product, Brand


from django.shortcuts import render,redirect,get_object_or_404


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# custom admin dashboard index view
class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        if request.user.is_admin:
            get_template_obj = SelectTemplate.objects.filter(is_active=True)
            # let check is template exists or not
            if get_template_obj.exists():
                temp = get_template_obj[0].category
            else:
                templates_count = SelectTemplate.objects.all().count()
                if templates_count < 1:
                    SelectTemplate.objects.create(user=request.user, category='1', is_active=True)
                if templates_count < 2:
                    SelectTemplate.objects.create(user=request.user, category='2', template_img='temp_demo/demo2.jpg')
                if templates_count < 3:
                    SelectTemplate.objects.create(user=request.user, category='3', template_img='temp_demo/demo3.jpg')

            total_order_number = Order.objects.filter(ordered=True).count()

            context = {
                "temp": temp,
                "total_order_number": total_order_number
            }
            return render(request, 'dashboard/index.html', context)

        else:
            return redirect('managetemplate:home')

    def post(self, request, *args, **kwargs):
        pass


# pages creating class view
class PagesTemplateView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        if request.user.is_admin:
            return render(request, 'dashboard/add_new_page.html')
        else:
            return redirect('managetemplate:home')

    def post(self, request, *args, **kwargs):
        if request.user.is_admin:
            if request.method == 'post' or request.method == 'POST':
                page_name = request.POST.get('page_name')

                if Pages.objects.filter(name=page_name).exists():
                    page_qs = Pages.objects.filter(name=page_name)
                    page_slug = page_qs[0].slug
                    return HttpResponseRedirect(reverse('dashboard:page', kwargs={'slug': page_slug}))

                elif(os.path.exists("templates/add_new_page/"+str(page_name)+".html")):
                    creating_page = Pages.objects.create(name=page_name)
                    current_page_slug = creating_page.slug
                    return HttpResponseRedirect(reverse('dashboard:page', kwargs={'slug': current_page_slug}))
                            
                else:
                    current_obj = Pages.objects.create(name=page_name)
                    page_slug = current_obj.slug
                    if(not os.path.exists("templates/add_new_page/"+str(page_name)+".html")):
                        with open("templates/add_new_page/"+ str(page_name) + ".html", "w") as f:
                            docs = '{% extends "dashboard/base.html" %} {% block body %} {% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>{{ title }}</h3><p class="text-subtitle text-muted">Super simple WYSIWYG editor. But you must include jQuery</p></div><div class="col-12 col-md-6 order-md-2 order-first"> <nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Summernote</li></ol> </nav></div></div></div> <section class="section"><div class="row"><div class="col-12"><div class="card"><div class="card-header"><h4 class="card-title">Default Editor</h4></div><div class="card-body"><form action="" method="post"> {% csrf_token %} {{form.media}} {{form.as_p}} <br> <br> <input type="submit" class="btn btn-primary" value="Save Data"></form></div></div></div></div> </section></div>{% endblock body %}'
                            f.write(docs)   
                        return HttpResponseRedirect(reverse('dashboard:page', kwargs={'slug': page_slug}))
                    else:
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return render(request, 'dashboard/add_new_page.html')
        
        else:
            return redirect('managetemplate:home')


# pages view
@login_required
def pages_view(request, slug):
    try:
        title = Pages.objects.get(slug=slug)
    except:
        title = Pages.objects.create(name=slug)
    page = title.name
    instance = get_object_or_404(Pages, slug=slug)
    form = PagesForm(request.POST or None ,instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    form = PagesForm(instance=instance)
    context = {
        'title': title,
        'form': form,
    }
    if(not os.path.exists("templates/add_new_page/"+str(page)+".html")):
        with open("templates/add_new_page/"+ str(page) + ".html", "w") as f:
            docs = '{% extends "dashboard/base.html" %} {% block body %} {% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>{{ title }}</h3><p class="text-subtitle text-muted">Super simple WYSIWYG editor. But you must include jQuery</p></div><div class="col-12 col-md-6 order-md-2 order-first"> <nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Summernote</li></ol> </nav></div></div></div> <section class="section"><div class="row"><div class="col-12"><div class="card"><div class="card-header"><h4 class="card-title">Default Editor</h4></div><div class="card-body"><form action="" method="post"> {% csrf_token %} {{form.media}} {{form.as_p}} <br> <br> <input type="submit" class="btn btn-primary" value="Save Data"></form></div></div></div></div> </section></div>{% endblock body %}'
            f.write(docs)
        return render(request, str("add_new_page/"+page+".html"), context)

    return render(request, str("add_new_page/"+page+".html"), context)


# pages list view
@login_required
def pageListView(request):
    pages_obj = Pages.objects.all().order_by('-id')
    context = {
        'pages_obj': pages_obj
    }
    return render(request, 'dashboard/pages_list.html', context)


# new pages details view
@login_required
def pageDetailView(request, slug):
    post = Pages.objects.get(slug=slug)
    context = {
        'post': post
    }
    if(not os.path.exists("templates/add_new_page/"+str(slug)+".html")):
        with open("templates/add_new_page/"+ str(slug) + ".html", "w") as f:
            docs = '{% extends "store_base.html" %}{% block store %}<main class="main"><br><br><section id="post-body"></section><br><br></main><script>window.addEventListener("DOMContentLoaded",()=>{const postBody=document.getElementById("post-body");console.log("{{post.body|escapejs}}");let body=JSON.parse("{{post.body|escapejs}}");let blocks=body.blocks;console.log(blocks.length);for(let index=0;index<=blocks.length;index++){console.log(blocks[index],index);switch(blocks[index].type){case"Header":let head=document.createElement(`h${blocks[index].data.level}`);head.textContent=blocks[index].data.text;postBody.appendChild(head);break;case"Image":let div=document.createElement("div");let image=document.createElement("img");let caption=document.createElement("small");image.src=`${blocks[index].data.file.url}`;image.style="margin-top:10px;";image.height=200;image.width=200;caption.textContent=blocks[index].data.caption;caption.style="margin-top:5px;";div.appendChild(image);div.appendChild(caption);div.style="width:30%;display:grid;place-items:center";postBody.appendChild(div);break;case"List":let list;if(blocks[index].data.style=="unordered"){list=document.createElement("ul");}else{list=document.createElement("ol");} for(const item in blocks[index].data.items){let li=document.createElement("li");li.textContent=blocks[index].data.items[item];list.appendChild(li);} postBody.appendChild(list);break;case"Raw":let blockquote=document.createElement("blockquote");let code=document.createElement("code");let pre=document.createElement("pre");pre.textContent=blocks[index].data.html;pre.style.background="#131313";pre.style.color="#dddddd";pre.style.padding="15px";code.appendChild(pre);postBody.appendChild(code);break;case"Attaches":let parent=document.createElement("div");parent.style="margin-top:10px;width:30%; padding:10px; border:1px solid black;border-radius:8px;";let a=document.createElement("a");let name=document.createElement("h4");a.href=`${blocks[index].data.file.url}`;a.textContent=`Download ${blocks[index].data.file.extension}(${blocks[index].data.file.size/1000}kb)`;a.style="grid-column: 1 / span 2";name.textContent=blocks[index].data.file.name;parent.appendChild(name);parent.appendChild(a);postBody.appendChild(parent);break;case"paragraph":const p=document.createElement("p");p.innerHTML=blocks[index].data.text;postBody.appendChild(p);break;case"Link":let parent2=document.createElement("div");let a2=document.createElement("a");parent2.style=" margin-top:10px; width:30%;display:grid; grid-template-columns: 1fr 50px; padding:10px; border:1px solid black;border-radius:8px;";if(blocks[index].data.meta.title){let title=document.createElement("p");title.textContent=blocks[index].data.meta.title;parent2.appendChild(title);} if(blocks[index].data.meta.image.url!==""){let parent3=document.createElement("div");let img=document.createElement("img");img.src=blocks[index].data.meta.image.url;parent3.style=" display:grid;place-items:center";img.height=40;img.width=40;parent3.appendChild(img);parent2.appendChild(parent3);} if(blocks[index].data.meta.description){let desc=document.createElement("small");desc.style="grid-column: 1 / span 2";desc.textContent=blocks[index].data.meta.description;parent2.appendChild(desc);} a2.style="text-decoration:none;color:black";a2.href=blocks[index].data.link;a2.appendChild(parent2);postBody.appendChild(a2);break;default:break;}}});</script>{% endblock store %}'
            f.write(docs)
        return render(request, str("add_new_page/"+slug+".html"), context)

    return render(request, str("add_new_page/"+slug+".html"), context)





# page title changing class view
class PageTitleTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = PageTitleForm()

        context = {
            "form": form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/dashboard/data_creation_form.html")):
            return render(request, 'dashboard/data_creation_form.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/dashboard/data_creation_form.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3">{{form.as_p}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'dashboard/data_creation_form.html', context)

    def post(self, request, *args, **kwargs):
        form = PageTitleForm()
        if request.method == 'post' or request.method == 'POST':
            form = PageTitleForm(request.POST, request.FILES)
            if form.is_valid():
                template_qs = SelectTemplate.objects.filter(is_active=True)[0]
                form_obj = form.save(commit=False)
                form_obj.active_template = template_qs
                form_obj.save()
                return redirect('dashboard:dashboard')
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        context = {
            'form': form
        }
        return render(request, 'dashboard/data_creation_form.html', context)



# fav icon changing class view
class ChangeFavIcon(TemplateView):
    def get(self, request, *args, **kwargs):
        form = FavIconForm()
        context = {
            'form': form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/dashboard/data_creation_form.html")):
            return render(request, 'dashboard/data_creation_form.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/dashboard/data_creation_form.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3">{{form.as_p}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'dashboard/data_creation_form.html', context)

    def post(self, request, *args, **kwargs):
        form = FavIconForm()
        if request.method == 'post' or request.method == 'POST':
            form = FavIconForm(request.POST, request.FILES)
            if form.is_valid():
                template_qs = SelectTemplate.objects.filter(is_active=True)[0]
                form_obj = form.save(commit=False)
                form_obj.active_template = template_qs
                form_obj.save()
                return redirect('dashboard:dashboard')
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        context = {
            'form': form
        }
        return render(request, 'dashboard/data_creation_form.html', context)

# application main logo changing class view
class ChangeMainIcon(TemplateView):
    def get(self, request, *args, **kwargs):
        form = MainIconForm()
        context = {
            'form': form
        }
        # check if data_creation.html file is exists or no
        # if exists return it else create this file and return it
        if(os.path.exists("templates/dashboard/data_creation_form.html")):
            return render(request, 'dashboard/data_creation_form.html', context)
        else:
            # creating new data_creation.html file with docs data
            with open("templates/dashboard/data_creation_form.html", "w") as f:
                docs = '{% extends "dashboard/base.html" %}{% block body %}{% include "dashboard/sidebar.html" %}<div class="page-heading"><div class="page-title"><div class="row"><div class="col-12 col-md-6 order-md-1 order-last"><h3>Change Favicon</h3></div><div class="col-12 col-md-6 order-md-2 order-first"><nav aria-label="breadcrumb" class="breadcrumb-header float-start float-lg-end"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Dashboard</a></li><li class="breadcrumb-item active" aria-current="page">Input Group</li></ol></nav></div></div></div><!-- Inputs Group with Buttons --><section id="input-group-buttons"><div class="row"><div class="col-12"><div class="card"><div class="card-content"><div class="card-body"><div class="row"><div class="col-md-10 mb-1"><form action="" method="post" enctype="multipart/form-data">{% csrf_token %}<div class="input-group mb-3">{{form.as_p}}<button class="btn btn-primary" type="submit" id="button-addon2">Add</button></div></form></div></div></div></div></div></div></div></section><!-- Inputs Group with Buttons end --></div>{% endblock body %}'
                f.write(docs)   
            return render(request, 'dashboard/data_creation_form.html', context)

    def post(self, request, *args, **kwargs):
        form = MainIconForm()
        if request.method == 'post' or request.method == 'POST':
            form = MainIconForm(request.POST, request.FILES)
            if form.is_valid():
                template_qs = SelectTemplate.objects.filter(is_active=True)[0]
                form_obj = form.save(commit=False)
                form_obj.active_template = template_qs
                form_obj.save()
                return redirect('dashboard:dashboard')
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        context = {
            'form': form
        }
        return render(request, 'dashboard/data_creation_form.html', context)





