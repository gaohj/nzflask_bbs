from django.core.cache import cache
from django.http import HttpResponse
def index(request):
    cache.set('qf','whpython',60)
    print(cache.get('qf'))
    response = HttpResponse(cache.get('qf'))
    return response