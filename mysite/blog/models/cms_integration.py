from django.db import models
from cms.models import CMSPlugin
from .mPost import Post


class BlogPluginModel(CMSPlugin):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title