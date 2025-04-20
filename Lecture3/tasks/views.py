from django.shortcuts import render, redirect
from django import forms

# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label='New task')



def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []

    ctx = {'tasks':request.session['tasks']}
    return render(request, 'tasks/index.html', ctx)

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            return redirect('tasks:index')
            
        else:
            ctx = {'form':form}
            return render(request, 'tasks/add.html', ctx)
        
    ctx = {'form': NewTaskForm()}
    return render(request, 'tasks/add.html', ctx)