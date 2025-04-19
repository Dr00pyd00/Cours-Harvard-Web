from django.shortcuts import render

# Create your views here.
tasks = ['foo', 'bar', 'baz']

def index(request):
    ctx = {'tasks':tasks}
    return render(request, 'tasks/index.html', ctx)
