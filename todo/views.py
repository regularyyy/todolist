from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/index.html', {'todo_list': todos})

def tasks_page(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/tasks_page.html', {'todo_list': todos})

@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    description = request.POST['description']
    tag = request.POST['tag']
    due_date = request.POST['due_date']
    todo = ToDo.objects.create(title=title, description=description, tag=tag, due_date=due_date)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('tasks_page')

def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('tasks_page')