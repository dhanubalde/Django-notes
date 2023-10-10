from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
def TaskList(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('-updated')
        context = {'tasks': tasks}
        return render(request, 'notes/index.html', context)
    
    if request.method == 'POST':
        task = Task.objects.create(body=request.POST.get('body'))
        task.save()
        return redirect('tasks')
    
    
def TaskDetail(request, pk):
    if request.method == 'GET':
        tasks = Task.objects.get(id=pk)
        context = {'tasks':tasks}
        return render(request, 'base/task.html', context)

    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        task.body = request.POST.get('body')
        task.save()
        return redirect('tasks')

## ------------------------------------------------------

def TaskDelete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

    context = {'task':task}   
    return render(request, 'base/delete.html', context)