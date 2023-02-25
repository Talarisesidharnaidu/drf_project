from rest_framework import serializers 
from watchlist_app.models import Movies

def name_length(value):
        if len(value) < 2:
            print("hello")
            raise serializers.ValidationError("name is too short")
        else:
            return value

class MovieSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    activate = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movies.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.activate = validated_data.get('activate',instance.activate)
        instance.save()
        return instance
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should not be same")
        else:
            return data
    
            
            