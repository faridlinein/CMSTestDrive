from django.db import models
from django.utils import timezone
from django.urls import reverse  # get_absolute_url
from django.contrib.auth.models import User
# ---Group 3rd-party apps
from taggit.managers import TaggableManager

"""NOTE_START 
There are two ways to add managers to your models: you can add extra manager methods 
or modify initial manager QuerySets. The first method provides you with a QuerySet API 
suchas Post.objects.my_manager(), and the latter provides you with Post.my_manager.all() . 
The manager will allow us to retrieve posts using Post.published.all() 
NOTE_END"""


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(
            PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()

    """NOTE_START 
     objects is the default manager of every model that retrieves all objects in the database. 
     However, we can also define custom managers for our models. 
    NOTE_END"""
    # ---Group ObjectManager
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    """NOTE_START  Canonical URLs for models
    You can use the post_detail URL that you have defined in the preceding section to build 
    the canonical URL for Post objects. The convention in Django is to add a get_absolute_url() method 
    to the model that returns the canonical URL of the object. For this method, we will use 
    the reverse() method that allows you to build URLs by their name and passing optional parameters.
    NOTE_END"""

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
