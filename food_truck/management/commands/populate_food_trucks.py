import csv
from django.core.management.base import BaseCommand
from food_truck.models import FoodTruckInfo  

from food_truck.utils.field_formatters import convert_date_to_desired_format as convert_date
from food_truck.utils.field_formatters import convert_decimal_format as convert_decimal

class Command(BaseCommand):
    help = 'Populate FoodTruckInfo model with data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_path']
        
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    food_truck = FoodTruckInfo(
                        location_id=row['locationid'],
                        applicant =row['Applicant'],
                        facility_type =row['FacilityType'],
                        cnn = row['cnn'],
                        location_description = row['LocationDescription'],
                        address = row['Address'],
                        block_lot = row['blocklot'],
                        block = row['block'],
                        lot = row['lot'],
                        permit = row['permit'],
                        status = row['Status'],
                        food_items = row['FoodItems'],
                        x_coordinates = row['X'],
                        y_coordinates = row['Y'],
                        latitude = row['Latitude'],
                        longitude = row['Longitude'],
                        schedule = row['Schedule'],
                        days_hours =str(row['dayshours']),
                        noi_sent = row['NOISent'],
                        approved = row['Approved'],
                        received = convert_date(row['Received']),
                        prior_permit = row['PriorPermit'],
                        expiration_date = convert_date(row['ExpirationDate']),
                        location = row['Location'],
                        fire_prevention_districts = row['Fire Prevention Districts'],
                        police_districts = row['Police Districts'],
                        supervisor_districts = row['Supervisor Districts'],
                        zip_codes = row['Zip Codes'],
                        neighborhoods_old = row['Neighborhoods (old)'],
                    )
                    food_truck.save()

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR('CSV file not found. Please provide a valid path.'))
        except Exception as e:
            failing_field = None  # Track the failing field
            for field_name, field_value in row.items():
                if str(field_value) in str(e):
                    failing_field = field_name
                    break

            if failing_field:
                self.stderr.write(self.style.ERROR(f'Error in field: {failing_field} - Error message: {str(e)}'))
            else:
                self.stderr.write(self.style.ERROR(f'An error occurred: {str(e)}'))

        else:
            self.stdout.write(self.style.SUCCESS('Successfully populated FoodTruckInfo model from CSV.'))
