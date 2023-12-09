from django.shortcuts import render

from static.STATICFILES_DIRS.scripts.api.cron.mai import get_all_rest

q = get_all_rest()
def index(request):
    data = {'date_book': q}
    return render(request, 'main.html', context=data)

