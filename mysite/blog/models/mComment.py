from django.db import models
# from django.utils import timezone
# from django.urls import reverse # get_absolute_url
# from django.contrib.auth.models import User

class Comment(models.Model):
    """NOTE_START 
    It contains ForeignKey to associate the
    comment with a single post. This many-to-one relationship is
    defined in the Comment model because each comment will be made on
    one post, and each post may have multiple comments.
    NOTE_END""" 
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
