from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from cute.models import MyCuteAngel


def angel(request):
    angel = MyCuteAngel.objects.filter(is_published=True).order_by('-date')
    paginator = Paginator(angel, 15)
    page = request.GET.get('page')
    try:
        angel = paginator.page(page)
    except PageNotAnInteger:
        angel = paginator.page(1)
    except EmptyPage:
        angel = paginator.page(paginator.num_pages)
    return render(request, 'cute/angel.html', {'angel': angel})
