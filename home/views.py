from django.shortcuts import render


def home_index(request):
    context = { }
    return render(request, 'home_index.html', context)

