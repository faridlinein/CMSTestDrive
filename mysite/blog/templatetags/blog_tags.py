from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

"""NOTE_START 
We have created a simple template tag that returns the number of
posts published so far. Each template tags module needs to contain
a variable called register to be a valid tag library. This variable is an
instance of template.Library , and it's used to register our own template
tags and filters. Then, we define a tag called total_posts with a Python
function and use the @register.simple_tag decorator to register the
function as a simple tag. Django will use the function's name as the
tag name. If you want to register it using a different name, you can
do it by specifying a name attribute, such as @register.simple_tag(name='my_tag') 

Before using custom template tags, you have to make them
available for the template using the {% load %} tag. As mentioned
before, you need to use the name of the Python module containing
your template tags and filters.
NOTE_END"""

register = template.Library()
@register.simple_tag()
def total_posts():
    return Post.published.count()


"""NOTE_START 
The power of custom template tags is that you can process any data
and add it to any template regardless of the view executed. You can
perform QuerySets or process any data to display results in your
templates.

Now, we will create another tag to display the latest posts in the
sidebar of our blog. This time, we will use an inclusion tag. Using an
inclusion tag, you can render a template with context variables
returned by your template tag. Edit the blog_tags.py file and add the
following code:
NOTE_END"""


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

    """NOTE_START 
    In the preceding code, we register the template tag
    using @register.inclusion_tag and specify the template that has to be
    rendered with the returned values using blog/post/latest_posts.html . Our
    template tag will accept an optional count parameter that defaults to
    5 . This parameter allows us to specify the number of posts we want
    to display. We use this variable to limit the results of the
    query Post.published.order_by('-publish')[:count] . Note that the function
    returns a dictionary of variables instead of a simple value. Inclusion
    tags have to return a dictionary of values, which is used as the
    context to render the specified template. The template tag we just
    created allows you to specify the optional number of posts to
    display as {% show_latest_posts 3 %} 
    NOTE_END"""


@register.simple_tag
def get_most_commented_posts(count=5):
    """NOTE_START 
    In addition to Count , Django offers the aggregation functions Avg , Max ,
    Min , and Sum . You can read more about aggregation functions at
    https://docs.djangoproject.com/en/2.0/topics/db/aggregation/ 
    NOTE_END"""
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    """NOTE_START 
    As you can see in the preceding screenshot, custom template filters
    are very useful to customize formatting. You can find more
    information about custom filters at
    https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/#writing-custom-
    template-filters 
    NOTE_END"""
    return mark_safe(markdown.markdown(text))
