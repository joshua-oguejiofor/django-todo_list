from django.urls import path
from . import views



urlpatterns = [
    path('', views.todo_list, name='todo_list'),                  # GET  /            -> list all todos
    path('create/', views.todo_create, name='todo_create'),       # GET/POST /create/ -> add a todo
    path('<int:pk>/edit/', views.todo_update, name='todo_update'),# GET/POST /1/edit/ -> edit a todo
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete'), # GET/POST /1/delete/ -> delete a todo
    path('<int:pk>/toggle/', views.todo_toggle, name='todo_toggle'), # POST /1/toggle/ -> mark complete/incomplete
]
