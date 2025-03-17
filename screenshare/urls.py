from django.urls import path
from stream.views import index, viewer

urlpatterns = [
    path('', index, name='home'),
    path('viewer/', viewer, name='viewer'),
]
