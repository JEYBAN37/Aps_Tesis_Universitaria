from django.urls import path
from .views import viewSociambiental

urlpatterns = [
    #  path('pollster/', Viewpollster.as_view(), name='page_pollster'),
    path('sociambiental/add/', viewSociambiental.add_items, name='add-items'),
    path('sociambiental/', viewSociambiental.view_items, name='view_items'),
    path('sociambiental/update/<int:serial_id>/', viewSociambiental.update_items, name='update-items'),
    path('sociambiental/<int:serial_id>/delete/', viewSociambiental.delete_items, name='delete-items'),
]
