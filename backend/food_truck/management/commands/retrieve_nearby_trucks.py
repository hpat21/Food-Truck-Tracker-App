from django.core.management.base import BaseCommand
from food_truck.models import FoodTruckInfo


class Command(BaseCommand):
    help = "Retrieve nearby food trucks using CLI"

    def add_arguments(self, parser):
        parser.add_argument("latitude", type=float, help="Latitude of the location")
        parser.add_argument("longitude", type=float, help="Longitude of the location")
        parser.add_argument("radius", type=float, help="Radius in miles")

    def handle(self, *args, **kwargs):
        latitude = kwargs["latitude"]
        longitude = kwargs["longitude"]
        radius = kwargs["radius"]

        nearby_trucks = FoodTruckInfo.get_nearby_trucks(latitude, longitude, radius)

        self.stdout.write("Nearby Food Trucks:")
        for truck in nearby_trucks:
            self.stdout.write(
                f"Name: {truck.applicant} | Distance: {truck.distance} miles"
            )
