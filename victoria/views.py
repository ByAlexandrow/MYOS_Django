from django.shortcuts import render


def victoria(request):
    template = 'victoria/victoria.html'
    return render(request, template)