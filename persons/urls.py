from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = 'persons'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<int:person_id>/', views.profile, name='profile'),
    path('todo-list/', views.person_todo_list, name='todo_list'),
    path('todo-list/create/', views.create_todo, name='create_todo'),
    path('todo-list/delate/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('todo-list/update/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('todo-list/change-status/<int:todo_id>/', views.change_todo_status, name='change_todo_status'),
    path('profile/settings/', views.profile_settings, name='profile_settings'),
]
