from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks_page', views.tasks_page, name='tasks_page'),
    path('add', views.add, name='add'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]