from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from .cms_menus import PollsMenu


@apphook_pool.register  # register the application
class PollsApphook(CMSApp):
    app_name = "polls"
    name = "Polls Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["polls.urls"]
    
    def get_menus(self, page=None, language=None, **kwargs):
        return [PollsMenu]