from rest_framework import viewsets

from food_truck.models import FoodTruckInfo
from .serializers import FoodTruckInfoSerializer

from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class FoodTruckInfoViewSet(viewsets.ModelViewSet):
    queryset = FoodTruckInfo.objects.all()
    serializer_class = FoodTruckInfoSerializer
    filterset_fields = ["latitude", "longitude"]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "latitude",
                openapi.IN_QUERY,
                description="Latitude of the location",
                type=openapi.TYPE_NUMBER,
            ),
            openapi.Parameter(
                "longitude",
                openapi.IN_QUERY,
                description="Longitude of the location",
                type=openapi.TYPE_NUMBER,
            ),
            openapi.Parameter(
                "radius",
                openapi.IN_QUERY,
                description="Radius for searching nearby food trucks",
                type=openapi.TYPE_NUMBER,
            ),
            openapi.Parameter(
                "cuisine",
                openapi.IN_QUERY,
                description="Filter food trucks by cuisine (this parameter should be added alone)",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
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
