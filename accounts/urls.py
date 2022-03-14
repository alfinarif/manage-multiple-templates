from os import name
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('account/register/', views.RegisterTemplateView.as_view(), name='register'),
    path('account/verification/<str:account_code>/', views.account_verification, name='verify'),
    path('account/login/', views.LoginTemplateView.as_view(), name='login'),

]
