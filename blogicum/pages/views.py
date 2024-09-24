from django.shortcuts import render


def about(request):
    """View about page."""
    return render(request, 'pages/about.html')


def rules(request):
    """View rules page."""
    return render(request, 'pages/rules.html')
