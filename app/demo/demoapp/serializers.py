from rest_framework import serializers
from demoapp.models import Dog, Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"
