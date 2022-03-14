from django.urls import path, include
from django.views.generic.base import View

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from api import views

# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'showorders', views.OrderListApiView, basename='showorders')

app_name = 'api'

urlpatterns = [
    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # product list api
    path('products/', views.ProductListApiView.as_view(), name='product_api'),
    # orders list api
    path('showorders/', views.OrderListApiView.as_view(), name='showorders'),

    # notification api
    path('orderNotify/', views.OrderNotificationApiView.as_view(), name='orderNotify'),
]
