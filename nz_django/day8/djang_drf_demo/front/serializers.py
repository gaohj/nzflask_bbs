from rest_framework import serializers
from .models import Book,Game,Movie,User
#HyperlinkedModelSerializer
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'b_name', 'b_price')

class Book2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'b_name', 'b_price')

class Book3Serializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    b_name = serializers.CharField()
    b_price = serializers.FloatField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(validated_data.get("b_name"))
        print(validated_data.get("b_price"))
        instance.b_name = validated_data.get("b_name") or instance.b_name
        instance.b_price = validated_data.get("b_price") or instance.b_price
        instance.save()
        return instance

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'g_name', 'g_price')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'm_name', 'm_price')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'u_name', 'm_password')