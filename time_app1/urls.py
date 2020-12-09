from django.urls import path     
from . import views

urlpatterns = [
    path('',views.first),
    path('time_display',views.index)
]