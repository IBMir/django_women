from django.urls import path
from women.views import *

urlpatterns = [
    path('', index),
    path('categor/<int:id>/', categor),
]
