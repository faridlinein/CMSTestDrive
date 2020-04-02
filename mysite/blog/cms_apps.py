from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register  # register the application
class BlogApphook(CMSApp):
    app_name = "blog"
    name = "Blog Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["blog.urls"]