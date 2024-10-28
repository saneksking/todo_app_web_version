from django.urls import path

from . import views


app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_index, name='admin_index'),
    path('person-change-activity/<int:person_id>/', views.person_change_activity, name='person_change_activity'),
    path('person-change-admin-status/<int:person_id>/',
         views.person_change_admin_status,
         name='person_change_admin_status'
         ),
    path('admin-person-settings/<int:person_id>/', views.admin_person_settings, name='admin_person_settings'),
    path('admin-person-delete/<int:person_id>/', views.admin_person_delete, name='admin_person_delete'),
]
