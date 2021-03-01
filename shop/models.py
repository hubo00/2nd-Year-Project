import uuid
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    products = models.ManyToManyField('Product', through="CatProd")

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:products_by_category', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    name_alt = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(500,500)],
    format='JPEG', options={'quality': 100})
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:prod_detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

class CatProd(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
