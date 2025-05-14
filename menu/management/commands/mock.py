from django.core.management import BaseCommand

from menu.models import MenuItem, Menu


def mock_menu(menu, parent=None, depth=1):
    if depth > 5:
        return
    for i in range(3):
        parend_title = parent.title.split('/')[1] if parent else ''
        sub = MenuItem.objects.create(
            menu=menu,
            title=f"{'sub'*depth}_{parend_title}/{i}", parent=parent
        )
        mock_menu(menu=menu, parent=sub, depth=depth+1)


class Command(BaseCommand):

    def handle(self, *args, **options):
        MenuItem.objects.all().delete()
        menu, _ = Menu.objects.get_or_create(name='main_menu')
        mock_menu(menu)
