from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            new_todo = Todo(
                title=request.POST['title'],
                user=request.user
            )
            new_todo.save()
            return redirect('index')

        todos = Todo.objects.filter(user=request.user)
        return render(request, 'index.html', {'todos': todos})
    else:
        return render(request, 'index.html', {'todos': []})


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
