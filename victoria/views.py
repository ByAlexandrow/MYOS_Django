from django.shortcuts import render
from django.core.paginator import Paginator

from victoria.models import Victoria


def victoria(request):
    moments = Victoria.objects.all().order_by('created_at')
    paginator = Paginator(moments, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'victoria/victoria.html', {'moments': page_obj})
