from django import template
from django.contrib.auth.models import User

from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category = None):
 return {'categories': Category.objects.all(), "current_category" : current_category}