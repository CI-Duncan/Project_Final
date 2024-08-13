from django.urls import path
from . import views


app_name = 'cms'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.client_list, name='client_list'),
    path('new/', views.client_new, name='client_new'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
    path('<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('note/<int:pk>/', views.note_content, name='note_content'),
    path('create-note/<int:pk>/', views.note_create, name='note_create'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
]