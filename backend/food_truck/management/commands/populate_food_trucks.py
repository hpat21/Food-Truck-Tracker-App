import csv
from django.core.management.base import BaseCommand
from food_truck.models import FoodTruckInfo

from food_truck.utils.field_formatters import (
    convert_date_to_desired_format as convert_date,
)
from food_truck.utils.field_formatters import fix_empty_value


class Command(BaseCommand):
    help = "Populate FoodTruckInfo model with data from CSV"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_path"]

        try:
            if FoodTruckInfo.objects.exists():
                self.stdout.write(
                    self.style.SUCCESS("FoodTruckInfo table already populated.")
                )
                return

            with open(csv_file, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    food_truck = FoodTruckInfo(
                        location_id=row["locationid"],
                        applicant=row["Applicant"],
                        facility_type=row["FacilityType"],
                        cnn=row["cnn"],
                        location_description=row["LocationDescription"],
                        address=row["Address"],
                        block_lot=row["blocklot"],
                        block=row["block"],
                        lot=row["lot"],
                        permit=row["permit"],
                        status=row["Status"],
                        food_items=row["FoodItems"],
                        x_coordinates=fix_empty_value(row["X"]),
                        y_coordinates=fix_empty_value(row["Y"]),
                        latitude=row["Latitude"],
                        longitude=row["Longitude"],
                        schedule=row["Schedule"],
                        days_hours=fix_empty_value(row["dayshours"]),
                        noi_sent=row["NOISent"],
                        approved=convert_date(row["Approved"]),
                        received=convert_date(row["Received"]),
                        prior_permit=row["PriorPermit"],
                        expiration_date=convert_date(row["ExpirationDate"]),
                        location=row["Location"],
                        fire_prevention_districts=fix_empty_value(
                            row["Fire Prevention Districts"]
                        ),
                        police_districts=fix_empty_value(row["Police Districts"]),
                        supervisor_districts=fix_empty_value(
                            row["Supervisor Districts"]
                        ),
                        zip_codes=fix_empty_value(row["Zip Codes"]),
                        neighborhoods_old=fix_empty_value(row["Neighborhoods (old)"]),
                    )
                    food_truck.save()

        except FileNotFoundError:
            self.stderr.write(
                self.style.ERROR("CSV file not found. Please provide a valid path.")
            )
        except Exception as e:
            failing_field = None  # Track the failing field
            for field_name, field_value in row.items():
                if str(field_value) in str(e):
                    failing_field = field_name
                    break

            if failing_field:
                self.stderr.write(
                    self.style.ERROR(
                        f"Error in field: {failing_field} - Error message: {str(e)}"
                    )
                )
            else:
                self.stderr.write(self.style.ERROR(f"An error occurred: {str(e)}"))

        else:
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully populated FoodTruckInfo model from CSV."
                )
            )
