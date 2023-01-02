from django.core.management import BaseCommand

from weather_check.alert import check_conditions


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        check_conditions()
