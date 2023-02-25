from rest_framework import serializers
from rest_framework.serializers import  ModelSerializer
from watchlist_app.models import Watchlist,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        #fields ="__all__"
        exclude = ('watchlist',)

class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
   # get_attribute = serializers.SerializerMethodField()
   # def get_get_attribute(self,object):
        #return len(object.name)
    class Meta:
        model = Watchlist
        #fields = ['id','name','description']
        fields = "__all__"
        #exclude = ['activate']
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"
                
# def name_length(value):
#         if len(value) < 2:
#             print("hello")
#             raise serializers.ValidationError("name is too short")
#         else:
#             return value
# def validate(self,data):
#             if data['name'] == data['description']:
#                 raise serializers.ValidationError("Title and Description should not be same")
#             else:
#                 return data  
# # class MovieSerializer(serializers.Serializer):
    
# #     id = serializers.IntegerField(read_only=True)
# #     name = serializers.CharField(validators=[name_length])
# #     description = serializers.CharField()
# #     activate = serializers.BooleanField()
    
# #     def create(self, validated_data):
# #         return Movies.objects.create(**validated_data)
    
# #     def update(self, instance, validated_data):
# #         instance.name = validated_data.get('name',instance.name)
# #         instance.description = validated_data.get('description',instance.description)
# #         instance.activate = validated_data.get('activate',instance.activate)
# #         instance.save()
# #         return instance
      
    
            
            