from django import forms
from django.forms import fields
from dashboard.models import Pages, PageTitle, FavIcon, MainIcon

class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ['body']

class PageTitleForm(forms.ModelForm):
    class Meta:
        model = PageTitle
        fields = ('title',)

class FavIconForm(forms.ModelForm):
    class Meta:
        model = FavIcon
        fields = ('image',)

class MainIconForm(forms.ModelForm):
    class Meta:
        model = MainIcon
        fields = ('image',)