from django.urls import path

from . import views
from posts.views import home_view
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', home_view, name='home_view')
]