from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
User = get_user_model()

from order.models import Order

class OrderNotification(models.Model):
    message = models.CharField(max_length=500, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Order)
def order_notification(sender, instance, created, **kwargs):
    if created:
        if instance.ordered:
            instance.save()
            message = f"{instance.user.username} has submit a new Order!"
            OrderNotification.objects.create(message=message, is_read=False)
    


class UserNotificationObject(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username


    @receiver(post_save, sender=User)
    def user_notification_object(sender, instance, created, **kwargs):
        if created:
            UserNotificationObject.objects.create(user=instance)
        instance.usernotificationobject.save()


class Notification(models.Model):
    user_obj = models.ManyToManyField(UserNotificationObject)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification', blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

