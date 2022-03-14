from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView, ListView

from dashboard.models import SelectTemplate, MainIcon, FavIcon, PageTitle
from store.models import Banner, PopupOffer, SmallBanner, AdsBanner, Category, Product, Brand

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from dashboard.models import MainIcon

# main templates index managing class view
class IndexTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        # template queryset
        get_template_obj = SelectTemplate.objects.filter(is_active=True)
        # let check is template exists or not
        if get_template_obj.exists():
            temp = get_template_obj[0].category
            
            # this condition will manage blog templates
            if temp == "1":
                
                
                context = {
                    "temp": temp,
                }
                return render(request, 'blog/blog.html', context)
            # blog condition end here

            # this condition will manage single vendor e-commerce template
            elif temp == "2":
                
                banners = Banner.objects.filter(is_active=True)
                small_banners = SmallBanner.objects.filter(is_active=True)
                ads_banners = AdsBanner.objects.filter(is_active=True)
                categories = Category.objects.all().order_by('-id')
                products = Product.objects.all().order_by('-id')
                recommend_products = Product.objects.all()[0:4]
                brands = Brand.objects.all().order_by('-id')[0:4]
                popupoffer = PopupOffer.objects.filter(is_active=True)

                context = {
                    "temp": temp,
                    "banners": banners,
                    "small_banners": small_banners,
                    "ads_banners": ads_banners,
                    "categories": categories,
                    "products": products,
                    "recommend_products": recommend_products,
                    "brands": brands,
                    "popupoffer": popupoffer
                }
                return render(request, 'store/index.html', context)
            # single vendor condition end here 
               
            # this condition will manage multi vendor e-commerce template
            elif temp == "3":
                return HttpResponse("Here will be multi vendor template")
            # multi vendor condition end here

            # this else condition if condition 1,2,3 return false then will redirect to the home page
            else:
                return redirect('managetemplate:home')
            # else condition end here
        
        # here is the else condition if template doesn't exists to the database then will show the default blog template
        else:
            # create default main logo and favicon
            page_title = PageTitle.objects.create(title='Home | Cleverange')
            main_logo = MainIcon.objects.create(active_template=0, image='main_icon/demo.png')
            favicon = FavIcon.objects.create(active_template=0, image='favicon/demo.png')
            # end here
            return render(request, 'blog/blog.html')
        # else condition end here



# select default templates class view
class SelectTemplateClassView(LoginRequiredMixin ,TemplateView):
    login_url = 'accounts:login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        if request.user.is_admin:
            # creating default templates
            templates = SelectTemplate.objects.all().order_by('-id')
            if not templates.exists():
                templates_count = SelectTemplate.objects.all().count()
                if templates_count < 1:
                    SelectTemplate.objects.create(user=request.user, category='1')
                if templates_count < 2:
                    SelectTemplate.objects.create(user=request.user, category='2', template_img='temp_demo/demo2.jpg')
                if templates_count < 3:
                    SelectTemplate.objects.create(user=request.user, category='3', template_img='temp_demo/demo3.jpg')

            context = {
                'templates': templates
            }
            
            return render(request, 'dashboard/select_template.html', context)
        else:
            return redirect('managetemplate:home')



# template select action function
class SelectTemplateAction(LoginRequiredMixin, TemplateView):
    login_url = 'accounts:login'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk, *args, **kwargs):
        if request.user.is_admin:
            make_first_deactive = SelectTemplate.objects.filter(is_active=True)
            for temp_obj in make_first_deactive:
                temp_obj.is_active = False
                temp_obj.save()
                # delete all exists data from database while changing the template
                delete_exists_pagetitle = PageTitle.objects.all().delete()
                delete_exists_mainlogo = MainIcon.objects.all().delete()
                delete_exists_favicon = FavIcon.objects.all().delete()
                delete_exists_category = Category.objects.all().delete()
                delete_exists_product = Product.objects.all().delete()
                delete_exists_banner = Banner.objects.all().delete()
                delete_exists_smallbanner = SmallBanner.objects.all().delete()
                delete_exists_adsbanner = AdsBanner.objects.all().delete()
                delete_exists_brand = Brand.objects.all().delete()
                # all data has been deleted
            obj_count = SelectTemplate.objects.filter(is_active=True).count()
            if obj_count == 0:
                get_template_obj = SelectTemplate.objects.get(id=pk)
                get_template_obj.user = request.user
                get_template_obj.is_active = True
                get_template_obj.save()

                # create default main logo and favicon
                page_title = PageTitle.objects.create(title='Home | Cleverange')
                main_logo = MainIcon.objects.create(active_template=0, image='main_icon/demo.png')
                favicon = FavIcon.objects.create(active_template=0, image='favicon/demo.png')
                # end here

                get_template_obj_cat = SelectTemplate.objects.filter(is_active=True)
                template_object = get_template_obj_cat[0].category
                if template_object == "1":
                    return redirect('managetemplate:home')

                if template_object == "2":
                    # create default data for single vendor
                    category_obj = Category.objects.create(name="Uncategorized")
                    # create 10 product at the same time
                    i = 1
                    while i < 11:
                        Product.objects.create(
                        name="Cleverange demo title",
                        category= category_obj,
                        preview_des="Hello CleaverCode",
                        description="Hello CleveRange",
                        price= 199,
                        old_price= 00.0
                        )
                        i += 1
                    
                    get_single_product = Product.objects.latest('created')
                    banner = Banner.objects.create(product=get_single_product, is_active=True)
                    adsbanner = AdsBanner.objects.create(product=get_single_product, is_active=True)
                    brand = Brand.objects.create(name="CleaverCode", image='demo/brand.png')
                    # create 3 small banner object at the same time
                    small_banner_count = SmallBanner.objects.all().count()
                    if small_banner_count < 1:
                        SmallBanner.objects.create(product=get_single_product, image='demo/banner-1.jpg', is_active=True) 
                    if small_banner_count < 2:
                        SmallBanner.objects.create(product=get_single_product, image='demo/banner-2.jpg', is_active=True)
                    if small_banner_count < 3:
                        SmallBanner.objects.create(product=get_single_product, image='demo/banner-1.jpg', is_active=True)
                    return redirect('managetemplate:home')

                if template_object == "3":
                    return redirect('managetemplate:home')
 
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        else:
            return redirect('managetemplate:home')



# template action status
@login_required
def template_status_action(request, pk):
    context = {
        'pk': pk
    }
    return render(request, 'dashboard/template_status.html', context)