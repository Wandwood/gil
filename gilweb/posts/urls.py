from django.urls import path

from . import views
from posts.views import detail_view, user_posts_create, user_posts_detail_view, user_search_view
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', user_posts_create, name='create'),
    path('detail/<int:my_id>/', detail_view, name='detail_view'),
    path('user_posts/', user_posts_detail_view, name='user_posts'),
    path('user_search', user_search_view, name='user_search')
]