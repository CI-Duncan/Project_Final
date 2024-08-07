from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('cms/', views.cms, name='cms'),
    path('list/', views.client_list, name='client_list'),
    path('new/', views.client_new, name='client_new'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
    path('<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('<int:pk>/delete/', views.client_delete, name='client_delete'),
]