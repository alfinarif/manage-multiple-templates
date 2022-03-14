from django.db import models
from django.urls import reverse
from accounts.models import User

# category
class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category', default="demo/demo.jpg")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Categories'
    
    def get_category_url(self):
        return reverse('store:update_category', kwargs={'pk': self.pk})
    
    def get_category_delete_url(self):
        return reverse('store:delete_category', kwargs={'pk': self.pk})

# home brand
class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_banner', default='product_banner/demo.jpg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_brand_url(self):
        return reverse('store:update_brand', kwargs={'pk': self.pk})
    
    def get_brand_delete_url(self):
        return reverse('store:delete_brand', kwargs={'pk': self.pk})


# products
class Product(models.Model):
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

    def get_product_url(self):
        return reverse('store:update_product', kwargs={'pk': self.pk})
    
    def get_product_delete_url(self):
        return reverse('store:delete_product', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created']

# home page main banner
class Banner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='banner')
    image = models.ImageField(upload_to='product_banner', default='product_banner/demo.jpg')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    
    def get_banner_url(self):
        return reverse('store:update_banner', kwargs={'pk': self.pk})
    
    def get_banner_delete_url(self):
        return reverse('store:delete_banner', kwargs={'pk': self.pk})

# home page small banner
class SmallBanner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='smallbanner')
    image = models.ImageField(upload_to='product_banner', default='product_banner/demo.jpg')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    
    def get_smallbanner_url(self):
        return reverse('store:update_smallbanner', kwargs={'pk': self.pk})
    
    def get_smallbanner_delete_url(self):
        return reverse('store:delete_smallbanner', kwargs={'pk': self.pk})

# home page ads banner
class AdsBanner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='adsbanner')
    image = models.ImageField(upload_to='product_banner', default='product_banner/demo.jpg')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    
    def get_adsbanner_url(self):
        return reverse('store:update_adsbanner', kwargs={'pk': self.pk})
    
    def get_adsbanner_delete_url(self):
        return reverse('store:delete_adsbanner', kwargs={'pk': self.pk})


# home page ads banner
class PopupOffer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='popupoffer')
    image = models.ImageField(upload_to='product_banner', default='product_banner/demo.jpg')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    
    # def get_adsbanner_url(self):
    #     return reverse('store:update_adsbanner', kwargs={'pk': self.pk})
    
    # def get_adsbanner_delete_url(self):
    #     return reverse('store:delete_adsbanner', kwargs={'pk': self.pk})


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
    
    def get_variation_url(self):
        return reverse('store:update_variation', kwargs={'pk': self.pk})
    
    def get_variation_delete_url(self):
        return reverse('store:delete_variation', kwargs={'pk': self.pk})
