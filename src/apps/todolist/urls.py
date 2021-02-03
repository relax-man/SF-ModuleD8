from django.urls import path
from apps.todolist.views import (
    CategoryListView,
    CategoryCreateView,
    CategoryDeleteView,
    TodoItemListView,
    TodoItemCreateView,
    TodoItemUpdateView,
    TodoItemDeleteView,
    TodoItemToggleCompleteView
)

app_name = 'todolist'

urlpatterns = [
    path(
        'list-category/',
        CategoryListView.as_view(),
        name='list_category'
    ),
    path(
        'create-category/',
        CategoryCreateView.as_view(),
        name='create_category'
    ),
    path(
        'delete-category/<int:pk>/',
        CategoryDeleteView.as_view(),
        name='delete_category'
    ),
    path(
        'list-item/',
        TodoItemListView.as_view(),
        name='list_item'
    ),
    path(
        'list-item/<int:priority>/',
        TodoItemListView.as_view(),
        name='list_item'
    ),
    path(
        'create-item/',
        TodoItemCreateView.as_view(),
        name='create_item'
    ),
    path(
        'update-item/<int:pk>/',
        TodoItemUpdateView.as_view(),
        name='update_item'
    ),
    path(
        'delete-item/<int:pk>/',
        TodoItemDeleteView.as_view(),
        name='delete_item'
    ),
    path(
        'toggle-complete/<int:pk>/',
        TodoItemToggleCompleteView.as_view(),
        name='toggle_complete'
    )
]