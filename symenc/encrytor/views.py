from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def users(request):
    now = datetime.now()
    context = {
        'current_date':now
    }
    return render(request,'users.html',context)


