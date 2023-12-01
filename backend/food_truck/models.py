from django.db import models
from geopy.distance import geodesic


# Create your models here.
class FoodTruckInfo(models.Model):
    location_id = models.IntegerField()
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100)
    cnn = models.IntegerField()
    location_description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    block_lot = models.CharField(max_length=255)
    block = models.CharField(max_length=50)
    lot = models.CharField(max_length=50)
    permit = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    food_items = models.TextField()
    x_coordinates = models.DecimalField(null=True, max_digits=18, decimal_places=10)
    y_coordinates = models.DecimalField(null=True, max_digits=18, decimal_places=10)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    schedule = models.TextField()
    days_hours = models.TextField(null=True, blank=True)
    noi_sent = models.CharField(max_length=255, null=True, blank=True)
    approved = models.DateField(null=True, blank=True)
    received = models.DateField(null=True, blank=True)
    prior_permit = models.IntegerField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    fire_prevention_districts = models.IntegerField(
        null=True,
    )
    police_districts = models.IntegerField(
        null=True,
    )
    supervisor_districts = models.IntegerField(
        null=True,
    )
    zip_codes = models.IntegerField(
        null=True,
    )
    neighborhoods_old = models.IntegerField(
        null=True,
    )

    @classmethod
    def get_nearby_trucks(cls, latitude, longitude, radius):
        """
        Retrieve nearby food trucks within a specified radius
        (in miles) of a given location.
        """
        user_location = (latitude, longitude)
        nearby_trucks = []
        all_trucks = cls.objects.all()

        for truck in all_trucks:
            truck_location = (truck.latitude, truck.longitude)
            distance = geodesic(user_location, truck_location).miles
            if distance <= radius:
                truck.distance = distance
                nearby_trucks.append(truck)

        return nearby_trucks

    @classmethod
    def filter_by_cuisine(cls, cuisine_type):
        """
        Filter food trucks by a specific cuisine type based on food items served.
        """
        filtered_trucks = cls.objects.filter(food_items__icontains=cuisine_type)
        return filtered_trucks

    def __str__(self):
        return self.applicant
