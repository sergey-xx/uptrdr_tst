from django.shortcuts import render


def index(request, pk=None):
    context = {}
    if pk:
        context['id'] = pk
    return render(request, 'index.html', context)
