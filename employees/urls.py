from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.employee_list_view, name='employee_list'),
    path('add/', views.employee_create_view, name='employee_create'),
    path('<int:pk>/', views.employee_detail_view, name='employee_detail'),
    path('<int:pk>/edit/', views.employee_update_view, name='employee_update'),
    path('<int:pk>/delete/', views.employee_delete_view, name='employee_delete'),
]
