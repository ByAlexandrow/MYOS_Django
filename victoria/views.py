from django.shortcuts import render

from victoria.models import Victoria


def victoria(request):
    moments = Victoria.objects.all().order_by('created_at')
    return render(request, 'victoria/victoria.html', {'moments': moments})
