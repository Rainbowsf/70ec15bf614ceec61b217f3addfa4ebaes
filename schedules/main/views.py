from django.shortcuts import render


def index(request):
    """
        Начальная страничка
    """
    return render(request, 'index.html')