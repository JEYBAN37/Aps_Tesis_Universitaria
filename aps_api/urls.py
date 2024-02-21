from django.urls import path
from .views import viewVivienda, viewInfoGeneral, viewFamilia, viewFamilyContext, viewBienestar, viewSaneamiento

urlpatterns = [
    #  path('pollster/', Viewpollster.as_view(), name='page_pollster'),

    #  Estas urls sirven para la gestion de datos de informacion general
    path('info_general/add/', viewInfoGeneral.add_items, name='add-items'),
    path('info_general/', viewInfoGeneral.view_items, name='view_items'),
    path('info_general/update/<int:serial_id>/', viewInfoGeneral.update_items, name='update-items'),
    path('info_general/<int:serial_id>/delete/', viewInfoGeneral.delete_items, name='delete-items'),

    path('vivienda/add/', viewVivienda.add_items, name='add-items'),
    path('vivienda/', viewVivienda.view_items, name='view_items'),
    path('vivienda/update/<int:serial_id>/', viewVivienda.update_items, name='update-items'),
    path('vivienda/<int:serial_id>/delete/', viewVivienda.delete_items, name='delete-items'),

    path('familia/add/', viewFamilia.add_items, name='add-items'),
    path('familia/', viewFamilia.view_items, name='view_items'),
    path('familia/update/<int:serial_id>/', viewFamilia.update_items, name='update-items'),
    path('familia/<int:serial_id>/delete/', viewVivienda.delete_items, name='delete-items'),

    path('contexto_familiar/add/', viewFamilyContext.add_items, name='add-items'),
    path('contexto_familiar/', viewFamilyContext.view_items, name='add-items'),
    path('contexto_familiar/update/<int:serial_id>/', viewFamilyContext.update_items, name='update-items'),
    path('contexto_familiar/<int:serial_id>/delete/', viewFamilyContext.delete_items, name='delete-items'),

    path('bienestar/add/', viewBienestar.add_items, name='add-items'),
    path('bienestar/', viewBienestar.view_items, name='add-items'),
    path('bienestar/update/<int:serial_id>/', viewBienestar.update_items, name='update-items'),
    path('bienestar/<int:serial_id>/delete/', viewBienestar.delete_items, name='delete-items'),

    path('saneamiento/add/', viewSaneamiento.add_items, name='add-items'),
    path('saneamiento/', viewSaneamiento.view_items, name='view_items'),
    path('saneamiento/update/<int:serial_id>/', viewSaneamiento.update_items, name='update-items'),
    path('saneamiento/<int:serial_id>/delete/', viewSaneamiento.delete_items, name='delete-items'),
]
