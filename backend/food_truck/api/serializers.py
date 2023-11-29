from rest_framework import serializers
from food_truck.models import FoodTruckInfo


class FoodTruckInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruckInfo
        fields = "__all__"
