from django.urls import path
from .views import index

app_name = 'menu'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', index, name='item'),
]
