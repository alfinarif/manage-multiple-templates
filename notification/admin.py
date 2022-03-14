from django.contrib import admin

from notification.models import UserNotificationObject, Notification, OrderNotification


admin.site.register(UserNotificationObject)
admin.site.register(Notification)
admin.site.register(OrderNotification)
