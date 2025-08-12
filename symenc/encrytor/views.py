from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def main(request):
    now = datetime.now()
    context = {
        'current_date':now
    }
    return render(request,'encrytor/main.html',context)


def login(request):
    context = {}
    return render(request, 'encrytor/login.html',context)
