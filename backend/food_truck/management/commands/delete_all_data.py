from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = "Delete all data from a specific model"

    def add_arguments(self, parser):
        parser.add_argument(
            "model_name", type=str, help="Name of the model to delete data from"
        )

    def handle(self, *args, **kwargs):
        model_name = kwargs["model_name"]
        try:
            Model = apps.get_model(
                app_label="food_truck", model_name=model_name
            )  # Replace 'myapp' with your app name
            if Model:
                Model.objects.all().delete()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully deleted all data from {model_name}."
                    )
                )
            else:
                self.stderr.write(self.style.ERROR(f"Model {model_name} not found."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {str(e)}"))
