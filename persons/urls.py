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
]
