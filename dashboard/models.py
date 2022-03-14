from typing import DefaultDict
from django.db import models
from django.db.models.fields import BigAutoField
from django_editorjs import EditorJsField
from django.urls import reverse
from accounts.models import User

class Pages(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    body=EditorJsField(
        editorjs_config={
            "tools":{
                "Link":{
                    "config":{
                        "endpoint":
                            '/linkfetching/'
                        }
                },
                "Image":{
                    "config":{
                        "endpoints":{
                            "byFile":'/uploadi/',
                            "byUrl":'/uploadi/'
                        },
                       
                    }
                },
                "Attaches":{
                    "config":{
                        "endpoint":'/uploadf/'
                    }
                }
            }
        }
    )

    def __str__(self):
        return self.name
    
    def get_page_url(self):
        return reverse('dashboard:pageDetail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        get_name = self.name.lower()
        self.slug = get_name.replace(" ", "-")
        return super().save(*args, **kwargs)


class SelectTemplate(models.Model):
    TEMPLATE_CATEGORY = (
        ('1', "Blog"),
        ('2', "E-shop single vendor"),
        ('3', "E-shop multi vendor")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='select_template')
    category = models.CharField(max_length=100, choices=TEMPLATE_CATEGORY, default=TEMPLATE_CATEGORY[0])
    template_img = models.ImageField(upload_to='template_img', default='temp_demo/demo.jpg')
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.category)


class PageTitle(models.Model):
    active_template = models.CharField(max_length=5, default='0', blank=True, null=True)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    


class FavIcon(models.Model):
    active_template = models.CharField(max_length=5, default='0', blank=True, null=True)
    image = models.ImageField(upload_to="favicon", default='favicon/demo.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.image)

class MainIcon(models.Model):
    active_template = models.CharField(max_length=5, default='0', blank=True, null=True)
    image = models.ImageField(upload_to="main_icon", default='main_icon/demo.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.image)