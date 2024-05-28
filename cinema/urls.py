from django.urls import path

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorDetail,
    ActorList
)

urlpatterns = [
    # path("movies/", MovieList.as_view(), name="movie-list"),
    # path("movies/<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail")
]

app_name = "cinema"
