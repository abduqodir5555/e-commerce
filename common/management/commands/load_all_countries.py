import json

from django.core.management.base import BaseCommand
from core.settings.base import BASE_DIR
from common.models import Country


class Command(BaseCommand):
    help = "Load all countries"

    def handle(self, *args, **kwargs):
        dir = BASE_DIR
        dir = str(dir)
        dir = dir.replace("\core", "")
        print(dir)
        try:
            with open(dir + '/data/countries.json' , 'r' ) as file:
                countries = json.load(file)
                for coun in countries:
                    Country.objects.get_or_create(name=coun['name_uz'], code=coun['code'])

            self.stdout.write(self.style.SUCCESS("Countries loaded successfully"))

        except Exception as e:
            print("error")
            self.stdout.write(self.style.ERROR(f"Error: {e}"))