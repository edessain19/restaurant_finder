from django.urls import path
from . import views


urlpatterns = [
    path('', views.request_create_view, name="home"),
]