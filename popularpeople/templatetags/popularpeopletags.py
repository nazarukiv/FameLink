from django import template
import popularpeople.views as views
from popularpeople.models import Category, TagPost
from popularpeople.utils import menu

register = template.Library()

@register.inclusion_tag('popularpeople/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('popularpeople/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}


@register.simple_tag
def get_menu():
    return menu