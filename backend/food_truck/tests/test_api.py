import json
from rest_framework import status
from django.utils import timezone
from django.http import response
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase, APIRequestFactory

from food_truck.models import FoodTruckInfo


class TestAPI(APITestCase):
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

        self.food_truck_data = {
            "id": 1071,
            "location_id": 1728067,
            "applicant": "Leo's Hot Dogs",
            "facility_type": "Push Cart",
            "cnn": 9121000,
            "location_description": "MISSION ST: 19TH ST to 20TH ST (2300 - 2399)",
            "address": "2301 MISSION ST",
            "block_lot": "3595031",
            "block": "3595",
            "lot": "031",
            "permit": "23MFF-00008",
            "status": "APPROVED",
            "food_items": "Hot dogs and related toppings: non alcoholic beverages",
            "x_coordinates": "6007018.0200000000",
            "y_coordinates": "2104913.0570000000",
            "latitude": "37.760086931987000",
            "longitude": "-122.418806481101000",
            "schedule": "http://testwebsite.com",
            "days_hours": None,
            "noi_sent": "",
            "approved": "2023-09-20",
            "received": "2023-09-20",
            "prior_permit": 1,
            "expiration_date": "2024-11-15",
            "location": "(37.76008693198698, -122.41880648110114)",
            "fire_prevention_districts": 2,
            "police_districts": 4,
            "supervisor_districts": 7,
            "zip_codes": 28859,
            "neighborhoods_old": 19,
        }

        self.url_food_trucks_list = reverse("food_truck:food-trucks-list")
        self.url_food_trucks_detail = reverse(
            "food_truck:food-trucks-detail", kwargs={"pk": self.food_truck.pk}
        )

    def test_get_food_trucks(self):
        """GET method for food trucks endpoint"""
        response = self.client.get(self.url_food_trucks_list, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_food_truck(self):
        """Test POST method for food trucks endpoint"""
        response = self.client.post(
            self.url_food_trucks_list, self.food_truck_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_destination(self):
        """Test PUT method for food trucks endpoint"""
        data = self.food_truck_data

        response = self.client.put(self.url_food_trucks_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_address(self):
        """Test DELETE method for food trucks endpoint"""
        response = self.client.delete(self.url_food_trucks_detail, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
