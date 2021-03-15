from django.shortcuts import get_object_or_404
from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db.models import Avg, Func

"""
I used a course on Udemy to learn how to use machine learning in the django framework
A part of it showed how to create a review model, I used it to create this model with additional functionality implemented by myself.
-- Hubert Bukowski x00161897
source = https://www.udemy.com/course/machine-learning-projects-recommendation-system-website/
"""

class Review(models.Model):
    RATING_OPTIONS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(CustomUser, default=None, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='user')
    title = models.CharField(max_length=80)
    content = models.TextField(max_length=256)
    image = models.ImageField(upload_to='review', blank=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200,200)],
    format='JPEG', options={'quality': 100})
    rating = models.FloatField(choices=RATING_OPTIONS, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id)