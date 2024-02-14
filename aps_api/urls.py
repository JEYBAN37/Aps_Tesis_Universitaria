from django.urls import path
from .views import Viewpollster

urlpatterns = [
    path('pollster/', Viewpollster.as_view(), name='page_pollster'),
    ]

