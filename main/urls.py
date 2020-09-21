from django.urls import path, re_path
import main.views as todo
from django.contrib import admin
# from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
  re_path(r'^$', todo.home, name='To Do Home'),
  path('add_todo/', todo.add_todo),
  path('delete_todo/<int:todo_id>/', todo.delete_todo),
]
