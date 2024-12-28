from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Todo
from .forms import TodoForm


@login_required
def home(request):
    todos = Todo.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo:home')
    else:
        form = TodoForm()

    return render(request, 'todo/home.html', {'todos': todos, 'form': form})


def toggle(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        todo.completed = not todo.completed
        todo.save()
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})
