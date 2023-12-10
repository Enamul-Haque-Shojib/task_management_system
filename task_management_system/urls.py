
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_tasks, name='show_tasks'),
    path('add/', include('tasks.urls'), name='add_task'),
    path('add/', include('categories.urls'), name='add_category'),
]
