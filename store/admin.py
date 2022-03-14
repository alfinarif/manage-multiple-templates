from django.contrib import admin

from store.models import (
    Category, Product, 
    ProductImages, Variations, 
    Banner, SmallBanner,
    AdsBanner,
    Brand,
    PopupOffer
    )

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class StoreAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ('id', 'name', 'category', 'price', 'is_stock')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'name',)
    
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image', 'is_active')

class SmallBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image', 'is_active')
    
class AdsBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image', 'is_active')
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

class PopupOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image', 'is_active')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, StoreAdmin)
admin.site.register(Variations)
admin.site.register(Banner, BannerAdmin)
admin.site.register(SmallBanner, SmallBannerAdmin)
admin.site.register(AdsBanner, AdsBannerAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(PopupOffer, PopupOfferAdmin)