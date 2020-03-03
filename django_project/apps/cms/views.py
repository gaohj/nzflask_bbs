from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST
# Create your views here.

@require_GET
def login_view(request):
    return render(request,'cms/login.html')
