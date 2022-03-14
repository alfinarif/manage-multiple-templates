from os import name
from django.urls import path

from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('cleverange/admin/index/', views.DashboardTemplateView.as_view(), name='dashboard'),
    
    # pages route view
    path('cleverange/admin/pages/', views.PagesTemplateView.as_view(), name='pages'),
    path('cleverange/admin/pages/all/', views.pageListView, name='allpages'),
    path('cleverange/admin/page/<slug:slug>/', views.pages_view, name='page'),
    path('<slug:slug>/', views.pageDetailView, name='pageDetail'),

    # change icon and title
    path('change/title/', views.PageTitleTemplateView.as_view(), name='title'),
    path('change/favicon/', views.ChangeFavIcon.as_view(), name='favicon'),
    path('change/logo/', views.ChangeMainIcon.as_view(), name='logo'),

]