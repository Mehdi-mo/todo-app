from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def tasks_list(request):

    if request.method == 'POST':
        body = request.POST.get('body')
        if body:
            Task.objects.create(body=body, user=request.user)
        return redirect('/')

    tasks = Task.objects.filter(user=request.user).order_by('-status', '-date_time_created')
    editing_id = request.GET.get('edit')  # check if user clicked edit on a task
    if editing_id:
        editing_id = int(editing_id)

    return render(request, 'tasks/tasks_list.html', {
        'tasks':tasks, 
        'editing_id':editing_id
        })

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        body = request.POST.get('body')
        if body:
            task.body = body 
            task.save()
    return redirect('/')


    

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
    return redirect('/')


@login_required
def task_toggle(request, task_id):
    task = get_object_or_404(Task, id= task_id)
    if request.method == 'POST':
        task.status = 'done' if task.status == 'pending' else 'pending'
        task.save()
    return redirect('/')
    
