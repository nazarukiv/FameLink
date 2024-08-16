menu = [
    {"name": "About Us", "url": "about"},
    {"name": "Add Article", "url": "add_page"},
    {"name": "Contact Us", "url": "contact"},
    {"name": "Log In", "url": "login"}
]
class DataMixin:
    title_page = None
    cat_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.title_page

    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context