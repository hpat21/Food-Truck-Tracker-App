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
