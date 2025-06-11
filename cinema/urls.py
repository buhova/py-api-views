from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreListView,
    GenreDetailView,
    ActorListView,
    ActorDetailView,
    CinemaHallListView,
    CinemaHallDetailView,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    # Movie (handled via router)
    path("", include(router.urls)),
    # Genre (APIView)
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    # Actor (GenericAPIView with mixins)
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    # CinemaHall (GenericViewSet-style using generic views)
    path("cinema_halls/", CinemaHallListView.as_view(), name="cinema-hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallDetailView.as_view(),
        name="cinema-hall-detail",
    ),
]

app_name = "cinema"
