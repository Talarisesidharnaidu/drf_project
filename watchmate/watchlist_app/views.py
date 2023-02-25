
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly 
from watchlist_app.permissions import AdminOrReadOnly
from watchlist_app.permissions import ReviewUserOrReadonly
from rest_framework import status
from rest_framework.exceptions import ValidationError
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework  import viewsets
from rest_framework import mixins
from rest_framework import generics
from watchlist_app.models import Watchlist,StreamPlatform,Review
from watchlist_app.serializers import (WatchlistSerializer, StreamPlatformSerializer,ReviewSerializer)

class ReviewCreate (generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        movie = Watchlist.objects.get(id=pk)
        review_user=self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("you have already entered")
        
        if movie.numbes_rating == 0:
            movie.avg_rating  = serializer.validated_data['rating']
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2
            
        movie.numbes_rating = movie.numbes_rating + 1
        movie.save()
        
            
        serializer.save(watchlist=movie,review_user=review_user)
    def get_queryset(self):
        return Review.objects.all()  
                     
class ReviewList(generics.ListAPIView):
    
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
   

class ReviewData(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=[ReviewUserOrReadonly]
   
    
# class ReviewData(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

    
# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    
            
class WatchListAv(APIView):
    
    def get(self,request):
        movie = Watchlist.objects.all()
        serializer = WatchlistSerializer(movie,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.error_messages)
        
class WatchDetailAv(APIView):
    def get(self,request,pk):
        try:
            movies = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error':' Not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchlistSerializer(movies)
        return Response(serializer.data)        
    
    def put(self,request,pk):
        movies = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movies = Watchlist.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class StreamPlatformAV(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
        
# class StreamPlatformAV(APIView):
    
#     def get(self,request):
#         platform = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platform,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) 
#         else:
#             return Response(serializer.error_messages)
        
class StreamPlatformDetailAv(APIView):
    
    def get(self,request,pk):
        try:
            platfom = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':' Not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(platfom)
        return Response(serializer.data)        
    
    def put(self,request,pk):
        updatplat = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(updatplat,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        delplatform = StreamPlatform.objects.get(pk=pk)
        delplatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   