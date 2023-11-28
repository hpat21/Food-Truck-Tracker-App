from rest_framework import viewsets
from food_truck.models import FoodTruckInfo
from .serializers import FoodTruckInfoSerializer

class FoodTruckInfoViewSet(viewsets.ModelViewSet):
    queryset = FoodTruckInfo.objects.all()
    serializer_class = FoodTruckInfoSerializer
