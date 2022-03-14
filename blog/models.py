from django.db import models
from django_editorjs import EditorJsField

from accounts.models import User


# category
class Category(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=255)
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
        return self.title
    
    # def get_post_url(self):
    #     return reverse('dashboard:pageDetail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        title = self.title.lower()
        self.slug = title.replace(" ", "-")
        return super().save(*args, **kwargs)