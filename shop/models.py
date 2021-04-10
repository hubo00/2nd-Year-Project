from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
from reviews.models import Review

# Category model which is Connected to the Subcategories via a Many to Many relationship
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:products_by_category', kwargs={'cat_slug':self.slug})

    def __str__(self):
        return self.name

# Subcategory model which acts as an intemediary between the Products and Category models
class subCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    category = models.ManyToManyField(Category, blank=False)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    # An Automatic save function which sets the slug to be a slugified version of the subcategory name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(subCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:products_by_subcategory', kwargs={'subcat_slug':self.slug})

    def __str__(self):
        return self.name

# Product model which is connected to the Subcategory model via a One-Many relationship
class Product(models.Model):
    name = models.CharField(max_length=250)
    name_alt = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    category = models.ForeignKey(subCategory, null=False, blank=False, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', default='product/DEFAULT/placeholder.png', blank=True)
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

    # An Automatic save function which sets the slug to be a concatenation of the product name and Alt-name
    def save(self, *args, **kwargs):
        if Product.name_alt:
            self.slug = slugify(self.name) + slugify(self.name_alt)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:prod_detail', kwargs={'prod_slug':self.slug})

    def __str__(self):
        return self.name

    # A function to get the average of all reviews for the specified product
    def get_review_avg(self):
        reviews = Review.objects.filter(product=self)
        count = len(reviews)
        sum = 0
        for review in reviews:
            sum += review.rating
        average = sum / count
        average = round(average, 0)
        return (average)