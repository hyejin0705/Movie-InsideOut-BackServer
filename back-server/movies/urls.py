from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    # path('create/', views.movie_create),

    path('popular/', views.movie_popular),
    path('recent/', views.movie_recent),
    # path('movies')

    path('<str:movie_id>/', views.movie_detail),
]
