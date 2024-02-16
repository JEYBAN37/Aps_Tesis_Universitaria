from django.urls import path
from .views.viewSociambiental import SociambientalCreate

urlpatterns = [
    #  path('pollster/', Viewpollster.as_view(), name='page_pollster'),
    path('questaSim/create/', SociambientalCreate.as_view(), name='encuesta-create'),

]
