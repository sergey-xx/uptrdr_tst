from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='items'
    )
    url = models.CharField(
        max_length=200,
        blank=True,
        help_text='Либо абсолютный URL, либо имя URL'
    )
    named_url = models.BooleanField(
        default=False,
        help_text='Если True — url считается именем URL'
    )
    is_open = False

    def __str__(self):
        return self.title
