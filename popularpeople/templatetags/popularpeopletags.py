from django import template
import popularpeople.views as views
from popularpeople.models import Category

register = template.Library()

@register.inclusion_tag('popularpeople/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}