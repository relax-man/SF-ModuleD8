from django.contrib import admin
from apps.todolist.models import Category, Priority, TodoItem

admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(TodoItem)
