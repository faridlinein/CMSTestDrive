from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse
from .models import Post


class BlogToolbar(CMSToolbar):

    supported_apps = ['blog']

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu(
            'blog',  # a unique key for this menu
            'Post',  # the text that should appear in the menu
        )

        menu.add_sideframe_item(
            name='Blog list',
            url=admin_reverse('blog_post_changelist'),
        )

        menu.add_modal_item(
            name='Add a new blog',
            url=admin_reverse('blog_post_add'),
        )

        buttonlist = self.toolbar.add_button_list()

        buttonlist.add_sideframe_button(
            name='Blog list',
            url=admin_reverse('blog_post_changelist'),
        )

        buttonlist.add_modal_button(
            name='Bclog a new poll',
            url=admin_reverse('blog_post_add'),
        )


# register the toolbar
toolbar_pool.register(BlogToolbar)
