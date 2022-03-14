from django.urls import path
from managetemplate import views

app_name = 'managetemplate'
urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='home'),
    # select template path
    path('manage-template/templates/', views.SelectTemplateClassView.as_view(), name='select_template'),
    path('manage-template/template/confirm/<int:pk>/', views.template_status_action, name='template_confirm'),
    path('manage-template/template/<int:pk>/', views.SelectTemplateAction.as_view(), name='select_template_action'),
]
