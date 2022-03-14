from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogTemplateView.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetailTemplateView.as_view(), name='blog_detail'),
]
