from django.urls import path

from . import views


app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_index, name='admin_index'),
]
