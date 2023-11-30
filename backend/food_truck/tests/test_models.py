from django.test import TestCase
from food_truck.models import FoodTruckInfo


class TestFoodTruckInfo(TestCase):
    """
    Class to test the system models.
    """

    def setUp(self):
        self.food_truck = FoodTruckInfo.objects.create(
            location_id=1728067,
            applicant="Leo's Hot Dogs",
            facility_type="Push Cart",
            cnn=9121000,
            location_description="MISSION ST: 19TH ST to 20TH ST (2300 - 2399)",
            address="2301 MISSION ST",
            block_lot=3595031,
            block=3595,
            lot=31,
            permit="23MFF-00008",
            status="APPROVED",
            food_items="Hot dogs and related toppings: non alcoholic beverages",
            x_coordinates=6007018.02,
            y_coordinates=2104913.057,
            latitude=37.76008693198698,
            longitude=-122.41880648110114,
            schedule="http://testwebsite.com",
            days_hours="Mo-We:7AM-7PM",
            noi_sent="Mo/Tu/We/Th/Fr:10AM-2PM",
            approved="2021-11-05",
            received="2021-11-05",
            prior_permit=2,
            expiration_date="2021-11-15",
            location="(37.76008693198698, -122.41880648110114)",
            fire_prevention_districts=2,
            police_districts=4,
            supervisor_districts=7,
            zip_codes=28859,
            neighborhoods_old=19,
        )
        self.food_truck.save()

    def test_food_truck_info_model(self):
        """
        Test FoodTruckInfo model.
        """

        self.assertEqual(self.food_truck.zip_codes, 28859)
        self.assertEqual(self.food_truck.block_lot, 3595031)
        self.assertEqual(self.food_truck.location_id, 1728067)
        self.assertEqual(self.food_truck.approved, "2021-11-05")
        self.assertNotEqual(self.food_truck.location_id, 123456)
        self.assertNotEqual(self.food_truck.approved, 3232323)
        self.assertNotEqual(self.food_truck.block_lot, str(3595031))
