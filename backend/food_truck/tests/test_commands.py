from django.core.management import call_command
from django.test import TestCase
from io import StringIO

from food_truck.models import FoodTruckInfo


class CommandTests(TestCase):
    """
    Test commands class.
    """

    def test_populate_food_trucks(self):
        """
        Test if the command 'populate_food_trucks'
        works as expected.
        """

        out = StringIO()

        food_trucks1 = FoodTruckInfo.objects.count()
        call_command("populate_food_trucks", "food-truck-data.csv", stdout=out)
        food_trucks2 = FoodTruckInfo.objects.count()

        self.assertTrue(food_trucks1 == 0)
        self.assertTrue(food_trucks2 >= 1)
        self.assertIn(
            "Successfully populated FoodTruckInfo model from CSV.", out.getvalue()
        )

    def test_delete_all_objects(self):
        """
        Test if the command 'delete_all_objects'
        works as expected.
        """

        out = StringIO()

        call_command("populate_food_trucks", "food-truck-data.csv", stdout=out)
        food_trucks1 = FoodTruckInfo.objects.count()
        call_command("delete_all_data", "FoodTruckInfo", stdout=out)
        food_trucks2 = FoodTruckInfo.objects.count()

        self.assertTrue(food_trucks1 >= 1)
        self.assertTrue(food_trucks2 == 0)
        self.assertIn(
            "Successfully deleted all data from FoodTruckInfo.", out.getvalue()
        )

    def test_retrieve_nearby_trucks(self):
        out = StringIO()
        latitude = 37.787988648995280
        longitude = -122.396100668471520
        radius = 0.001

        call_command("populate_food_trucks", "food-truck-data.csv", stdout=out)
        call_command(
            "retrieve_nearby_trucks",
            str(latitude),
            str(longitude),
            str(radius),
            stdout=out,
        )

        output = out.getvalue()

        # Remove the undesired message from the output
        output_lines = output.split("\n")
        filtered_output = "\n".join(
            line
            for line in output_lines
            if "Successfully populated FoodTruckInfo model from CSV." not in line
        )

        self.assertIn("Nearby Food Trucks:", filtered_output)
        self.assertIn("Name: Bonito Poke | Distance: 0.0 miles", filtered_output)
        self.assertIn("Name: Papalote Inc. | Distance: 0.0 miles", filtered_output)
        self.assertIn("Name: Truly Food & More | Distance: 0.0 miles", filtered_output)
