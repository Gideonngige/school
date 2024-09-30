from rest_framework import serializers

class StoreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

class ForestSerializer(serializers.Serializer):
    county = serializers.CharField(max_length=40)
    forest = serializers.CharField(max_length=40)
    area_square = serializers.DecimalField(decimal_places=2, max_digits=10)