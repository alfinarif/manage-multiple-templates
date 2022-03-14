from django.db import models
from django.urls import reverse

from accounts.models import User

# category
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category')
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category', default="demo/demo.jpg")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Categories'

# home brand
class Brand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='brand')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_banner', default='product_banner/demo.jpg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# products
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand', blank=True, null=True)
    preview_des = models.TextField(max_length=200, verbose_name='Preview Description')
    description = models.TextField(max_length=1000, verbose_name="Description")
    image = models.ImageField(upload_to='products', default="demo/demo.jpg")
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    is_stock = models.BooleanField(default=True)
    is_slider = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # def get_product_url(self):
    #     return reverse('store:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created']

# home page main banner
class Banner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='banner')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='banner')
    image = models.ImageField(upload_to='product_banner', default='product_banner/demo.jpg')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

# home page small banner
class SmallBanner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='smallbanner')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='smallbanner')
    image = models.ImageField(upload_to='product_banner', default='product_banner/demo.jpg')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

# home page ads banner
class AdsBanner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adsbanner')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='adsbanner')
    image = models.ImageField(upload_to='product_banner', default='product_banner/demo.jpg')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name



# product image gallery
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to='product_gallery')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)

# custom manager for variations
class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation='size')

    def colors(self):
        return super(VariationManager, self).filter(variation='color')

# variations 
class Variations(models.Model):
    VARIATIONS_TYPE = (
    ('size', 'size'),
    ('color', 'color'),
    )
    variation = models.CharField(max_length=100, choices=VARIATIONS_TYPE)
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return self.name
