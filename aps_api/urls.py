from django.urls import path
from .views import viewSociambiental
from .views import viewVivienda

urlpatterns = [
    #  path('pollster/', Viewpollster.as_view(), name='page_pollster'),

    #  Estas urls sirven para la gestion de datos de informacion general
    path('sociambiental/add/', viewSociambiental.add_items, name='add-items'),
    path('sociambiental/', viewSociambiental.view_items, name='view_items'),
    path('sociambiental/update/<int:serial_id>/', viewSociambiental.update_items, name='update-items'),
    path('sociambiental/<int:serial_id>/delete/', viewSociambiental.delete_items, name='delete-items'),

    path('vivienda/add/', viewVivienda.add_items, name='add-items'),
    path('vivienda/', viewVivienda.view_items, name='view_items'),
    path('vivienda/update/<int:serial_id>/', viewVivienda.update_items, name='update-items'),
    path('vivienda/<int:serial_id>/delete/', viewVivienda.delete_items, name='delete-items'),
]
