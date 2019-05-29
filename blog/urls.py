from django.urls import path
from . import views


urlpatterns = [
    path('', views.rate_list, name='rate_list'),
]
