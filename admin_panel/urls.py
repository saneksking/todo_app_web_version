from django.urls import path

from . import views


app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_index, name='admin_index'),
    path('person-change-activity/<int:person_id>/', views.person_change_activity, name='person_change_activity'),
]