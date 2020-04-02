from django.contrib.sitemaps import Sitemap
from .models import Post

"""NOTE_START 
You can take a look at the complete sitemap reference in
the official Django documentation located
at https://docs.djangoproject.com/en/2.0/ref/contrib/sitemaps/ 
NOTE_END"""


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
