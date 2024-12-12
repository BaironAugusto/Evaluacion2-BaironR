from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('editar/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),  # Nueva URL para editar tarea  
]



