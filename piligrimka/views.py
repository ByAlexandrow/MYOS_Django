from django.shortcuts import render

from piligrimka.models import Piligrimka


def piligrimka(request):
    moments = Piligrimka.objects.all().order_by('-created_at')
    return render(request, 'piligrimka/piligrimka.html', {'moments': moments})
