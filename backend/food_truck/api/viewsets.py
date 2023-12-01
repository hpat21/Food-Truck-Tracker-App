from rest_framework import viewsets
from food_truck.models import FoodTruckInfo
from .serializers import FoodTruckInfoSerializer

from rest_framework.response import Response


class FoodTruckInfoViewSet(viewsets.ModelViewSet):
    queryset = FoodTruckInfo.objects.all()
    serializer_class = FoodTruckInfoSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ["latitude", "longitude"]

    def list(self, request):
        latitude = request.query_params.get("latitude")
        longitude = request.query_params.get("longitude")
        radius = request.query_params.get("radius")
        cuisine = request.query_params.get("cuisine")

        if cuisine:
            return self.list_by_cuisine(request, cuisine)

        if latitude and longitude and radius:
            return self.list_by_location_and_radius(
                request, latitude, longitude, radius
            )

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def list_by_cuisine(self, request, cuisine):
        return_trucks_by_cuisine = FoodTruckInfo.filter_by_cuisine(cuisine)
        serializer = self.get_serializer(return_trucks_by_cuisine, many=True)
        return Response(serializer.data)

    def list_by_location_and_radius(self, request, latitude, longitude, radius):
        try:
            latitude = float(latitude)
            longitude = float(longitude)
            radius = float(radius)
        except ValueError:
            return Response(
                {
                    "error": "Invalid parameter values. Latitude, longitude, and radius must be numeric"
                },
                status=400,
            )

        nearby_trucks = FoodTruckInfo.get_nearby_trucks(latitude, longitude, radius)
        serializer = self.get_serializer(nearby_trucks, many=True)
        return Response(serializer.data)
