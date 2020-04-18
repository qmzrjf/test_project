from django.core.management.base import BaseCommand, CommandError
from profile_app.models import Customer, Logger, LoggerEditProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        list_of_models = [Customer, Logger, LoggerEditProfile]
        for model in list_of_models:
            name_model = str(model.__name__)
            list_of_model_fields = [x for x in model().__dict__.keys() if not x.startswith('_')]
            count_of_objects = model.objects.all().count()
            print(f'Name of model: {name_model}' + '\n' +
                  f'Fields: {list_of_model_fields}' + '\n' +
                  f'Count objects: {count_of_objects}' + '\n' +
                  '__________________________________')
