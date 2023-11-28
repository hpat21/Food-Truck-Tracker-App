from django.urls import path, include
from .api.viewsets import FoodTruckInfoViewSet

from rest_framework import routers

app_name = "food_truck"

router = routers.DefaultRouter()

router.register(r"food-trucks", FoodTruckInfoViewSet, basename="food-trucks")

urlpatterns = [
    path("", include(router.urls)),
]
