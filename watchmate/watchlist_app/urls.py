
from django.urls import path, include
#from watchlist_app.views import movie_list,movie_details
#from watchlist_app.views import MovieListAv,MovieDetailAv
from rest_framework.routers import DefaultRouter

from watchlist_app.views import (WatchListAv, WatchDetailAv, StreamPlatformAV, StreamPlatformDetailAv,ReviewCreate,ReviewList,ReviewData)

router = DefaultRouter()
router.register('stream',StreamPlatformAV,basename='streamplatform')     

urlpatterns = [
    #path('',movie_list,name='movielist'),
    #path('<int:pk>/',movie_details,name='moviedetails'),
    path('', WatchListAv.as_view(),name='movie-list'),
    path('list/<int:pk>/',WatchDetailAv.as_view(),name='movie-details'),
    path('',include(router.urls)),
    #path('stream/',StreamPlatformAV.as_view(),name="stream-Platform"),
    #path('stream/<int:pk>/',StreamPlatformDetailAv.as_view(), name='stream-details'),
    #path('review/',ReviewList.as_view(),name="review-list"),
    #path('review/<int:pk>/',ReviewData.as_view(),name="review-data"),
    path('stream/<int:pk>/reviewcreate/',ReviewCreate.as_view(),name="review-create"),
    path('stream/<int:pk>/review/',ReviewList.as_view(),name="review-list"),
    path('review/<int:pk>/',ReviewData.as_view(),name="review-data"),
    #path('stream/<int:pk>/reviewcreate/',ReviewCreate.as_view(),name="review-create"),
    
]