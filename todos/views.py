from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


# READ: show all todos on the home page
def todo_list(request):
    # Fetch every Todo row from the database (already ordered by Meta.ordering)
    todos = Todo.objects.all()
    # Render the list template, passing the todos into the template context
    return render(request, 'todos/todo_list.html', {'todos': todos})


# CREATE: add a new todo
def todo_create(request):
    if request.method == 'POST':
        # Bind submitted form data to the form
        form = TodoForm(request.POST)
        if form.is_valid():
            # Saves a new Todo row to the database
            form.save()
            # Show a success message on the next page
            # Redirect back to the list page (prevents duplicate submits on refresh)
            return redirect('todo_list')
    else:
        # GET request: show a blank form
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form, 'title': 'Add Todo'})


# UPDATE: edit an existing todo
def todo_update(request, pk):
    # Fetch the Todo by primary key, or return a 404 page if it doesn't exist
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        # Bind submitted data to the form AND link it to the existing object
        # so save() updates the row instead of creating a new one
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        # GET request: pre-fill the form with the existing todo's data
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form, 'title': 'Edit Todo'})


# DELETE: remove a todo (with a confirmation page)
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        # Only actually delete once the user confirms via POST
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})


# Quick action: toggle a todo's completed status directly from the list page
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    # Flip True/False
    todo.completed = not todo.completed
    # Only update the 'completed' column for efficiency
    todo.save(update_fields=['completed'])
    return redirect('todo_list')
