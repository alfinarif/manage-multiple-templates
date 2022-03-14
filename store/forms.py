from django import forms
from django.forms import fields
from store.models import (
    Category, Product, 
    Variations, 
    Banner, SmallBanner,
    AdsBanner,
    Brand
    )

# ads banner form
class AdsBannerCreationForm(forms.ModelForm):
    class Meta:
        model = AdsBanner
        fields = [
            'product',
            'image',
            'is_active'
            ]

# small banner form
class SmallBannerCreationForm(forms.ModelForm):
    class Meta:
        model = SmallBanner
        fields = [
            'product',
            'image',
            'is_active'
            ]

# main banner form
class BannerCreationForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = [
            'product',
            'image',
            'is_active'
            ]


# product category form
class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'parent',
            'name',
            'image'
            ]

# product brand form
class BrandCreationForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            'name',
            'image'
            ]

# product form
class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'preview_des',
            'description',
            'image',
            'price',
            'old_price'
            ]

# product variations form
class VariationsCreationForm(forms.ModelForm):
    class Meta:
        model = Variations
        fields = [
            'variation',
            'name',
            'product',
            'price'
            ]




