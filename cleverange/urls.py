
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt


from cleverange import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('accounts.urls')),
    path('', include('dashboard.urls')),
    path('blog/', include('blog.urls')),
    path('', include('managetemplate.urls')),

    path('cleverange/admin/store/', include('store.urls')),
    path('orders/', include('order.urls')),
    
    # path("notification/", include('notification.urls')),

    # api route
    path("api/", include('api.urls')),
    
    #path for editorJs
    path('uploadi/',csrf_exempt(views.uploadi) ),
    path('uploadf/',csrf_exempt(views.uploadf) ),
    path('linkfetching/',views.upload_link_view),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)