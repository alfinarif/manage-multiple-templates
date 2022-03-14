from django.urls import path
from store import views

app_name = 'store'
urlpatterns = [
    # Banners Route Start From Here
    path('banners/main/', views.BannerList.as_view(), name='main_banner'),
    path('banners/main/create/', views.MainBannerCreationTemplateView.as_view(), name='create_main_banner'),
    path('banners/small/', views.SmallBannerList.as_view(), name='small_banner'),
    path('banners/small/create/', views.SmallBannerCreationTemplateView.as_view(), name='create_small_banner'),
    path('banners/ads/', views.AdsBannerList.as_view(), name='ads_banner'),
    path('banners/ads/create/', views.AdsBannerCreationTemplateView.as_view(), name='create_ads_banner'),

    # Data fatching Route Here
    path('product/', views.ProductList.as_view(), name='product_list'),
    path('product/categories/', views.CategoryList.as_view(), name='category_list'),
    path('product/brands/', views.BrandList.as_view(), name='brand_list'),
    path('product/variations/', views.VariationList.as_view(), name='variation_list'),

    # Creation Route Start From Here
    path('product/categories/add-new/', views.CategoryCreationTemplateView.as_view(), name='create_category'),
    path('product/add-new/', views.ProductCreationTemplateView.as_view(), name='create_product'),
    path('product/brands/add-new/', views.BrandCreationTemplateView.as_view(), name='create_brand'),
    path('product/variations/add-new/', views.VariationCreationTemplateView.as_view(), name='create_variation'),

    # Update Object Route Start From Here
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('product/categories/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='update_category'),
    path('product/variations/update/<int:pk>/', views.VariationUpdateView.as_view(), name='update_variation'),
    path('product/brands/update/<int:pk>/', views.BrandUpdateView.as_view(), name='update_brand'),
    path('product/banner/update/<int:pk>/', views.BannerUpdateView.as_view(), name='update_banner'),
    path('product/smallbanner/update/<int:pk>/', views.SmallBannerUpdateView.as_view(), name='update_smallbanner'),
    path('product/adsbanner/update/<int:pk>/', views.AdsBannerUpdateView.as_view(), name='update_adsbanner'),

    # Delete Object Route Start From Here
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('product/category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('product/variation/delete/<int:pk>/', views.VariationDeleteView.as_view(), name='delete_variation'),
    path('product/brand/delete/<int:pk>/', views.BrandDeleteView.as_view(), name='delete_brand'),
    path('product/banner/delete/<int:pk>/', views.BannerDeleteView.as_view(), name='delete_banner'),
    path('product/smallbanner/delete/<int:pk>/', views.SmallBannerDeleteView.as_view(), name='delete_smallbanner'),
    path('product/adsbanner/delete/<int:pk>/', views.AdsBannerDeleteView.as_view(), name='delete_adsbanner'),

]
