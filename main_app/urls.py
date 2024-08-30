from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.render_index, name="index"),
    
    path("page_1", views.render_page_1, name="python_introduction"),

    path("page_2/", views.render_page_2, name="python_base"),
    path("page_2/condition_operators", views.render_page_cond_operators, name="cond_operators"),
    path("page_2/cycles", views.render_page_cycles, name="cycles"),
]
