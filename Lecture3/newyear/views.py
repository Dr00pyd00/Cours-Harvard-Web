from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    ctx = {"newyear": now.month == 1 and now.day ==1}
    return render(request, 'newyear/index.html', ctx)