
from django.shortcuts import render
from tasks.models import Task

# Create your views here.

def show_tasks(request):
    data = Task.objects.all()
   
    return render(request, 'show_tasks.html', {'data': data})