import re

from django import template
from django.urls import reverse

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):

    def open_items(items, currend_id):
        if not currend_id:
            return
        current_lst = [item for item in items if item.id == currend_id]
        if not current_lst:
            return
        current = current_lst[0]
        current.is_open = True
        open_items(items, current.parent_id)

    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent_id == (parent.id if parent else None):
                tree.append({
                    'item': item,
                    'children': build_tree(items, item),
                    'is_open': item.is_open,
                    'url': reverse('menu:item', kwargs={'pk': item.pk}),
                    'is_active': True,
                })
        return tree

    request = context['request']
    current_id_str = re.sub(r'\D', '', request.path)
    current_id = int(current_id_str) if current_id_str else None
    items = MenuItem.objects.filter(menu__name=menu_name)
    if not items:
        return {'menu_items': []}

    open_items(items, current_id)
    return {'menu_items': build_tree(items), 'request': request}
