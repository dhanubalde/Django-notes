from django.shortcuts import render, redirect
from django.views import View
from .models import Task
# Create your views here.
# FUNCTION VIEWS
# def TaskList(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all().order_by('-updated')
#         context = {'tasks': tasks}
#         return render(request, 'notes/index.html', context)
    
#     if request.method == 'POST':
#         task = Task.objects.create(body=request.POST.get('body'))
#         task.save()
#         return redirect('tasks')
class TaskList(View):

    def get(self, request):
        tasks = Task.objects.all().order_by('-updated')
        context = {'tasks':tasks}
        return render(request, 'notes/index.html', context)

    def post(self, request):
        task = Task.objects.create(
            body=request.POST.get('body')
        )
        task.save()
        return redirect('tasks')
    
# def TaskDetail(request, pk):
#     if request.method == 'GET':
#         tasks = Task.objects.get(id=pk)
#         context = {'tasks':tasks}
#         return render(request, 'notes/task.html', context)

#     if request.method == 'POST':
#         task = Task.objects.get(id=pk)
#         task.body = request.POST.get('body')
#         task.save()
#         return redirect('tasks')

class TaskDetail(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        context = {'task':task}
        return render(request, 'notes/task.html', context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.body = request.POST.get('body')
        task.save()
        return redirect('tasks')
## ------------------------------------------------------

# def TaskDelete(request, pk):
#     task = Task.objects.get(id=pk)

#     if request.method == 'POST':
#         task.delete()
#         return redirect('tasks')

#     context = {'task':task}   
#     return render(request, 'notes/delete.html', context)

class TaskDelete(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        context = {'task':task}   
        return render(request, 'notes/delete.html', context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('tasks')