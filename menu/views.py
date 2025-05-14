from django.shortcuts import render


def index(request, pk=None):
    context = {}
    return render(request, 'index.html', context)
