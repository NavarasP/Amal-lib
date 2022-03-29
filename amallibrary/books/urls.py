from django.urls import URLPattern, path
from . import views
from .views import *

urlpatterns = [

    path('Bookstall', Bookstall.as_view(), name='Bookstall'),
    path('Viewbook', views.Viewbook, name='Viewbook'),
    path('Returnbook/<int:id>', views.Returnbook, name='Returnbook'),
    path('Editbook/<int:id>', views.Editbook, name='Editbook'),
    path('Deletebook/<int:id>', views.Deletebook, name='Deletebook'),
    path('Adminbook', views.Adminbook, name='Adminbook'),


]
