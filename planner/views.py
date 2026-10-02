from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
# Create your views here.

def home(request):
    tasks = Task.objects.all() #This helps to fetch all the data from the database
    return render(request, 'home.html',{"tasks": tasks}) #This will render the data to the home.html file (calling of web page)

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        subject = request.POST['subject']
        deadline = request.POST['deadline']

        Task.objects.create(
            title=title, 
            subject=subject, 
            deadline=deadline
        )
        return redirect('home') #This will redirect to the home page after adding a task
    return render(request, 'add_task.html') #This will render the add_task.html file (calling of web page)

def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect('home')

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.subject = request.POST['subject']
        task.deadline = request.POST['deadline']
        task.save()
        return redirect('home')
    return render(request, 'edit_task.html', {'task': task})