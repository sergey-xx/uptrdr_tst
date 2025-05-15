from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):

    def get_id(context):
        for _ in context:
            current_id = context.get('id')
            if current_id:
                return current_id

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
                item.cldrn = build_tree(items, item)
                tree.append(item)
        return tree

    request = context['request']
    current_id = get_id(context)
    items = MenuItem.objects.filter(menu__name=menu_name)
    if not items:
        return {'menu_items': []}

    open_items(items, current_id)
    return {'menu_items': build_tree(items), 'request': request}
