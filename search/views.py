from django.shortcuts import render
from .logic import words


def search_view(request):
    if request.method == 'GET':
        return render(request, 'search/template.html')
    string = words(request.POST.get('key'))
    context = {'words': string}
    return render(request, 'search/view.html', context=context)
