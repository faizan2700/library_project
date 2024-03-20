from django.core.management.base import BaseCommand
from main.dump.move_data import clean_data
class Command(BaseCommand):
    help = 'This command truncates records in all tables in database.'

    def handle(self, *args, **options): 
        clean_data() 
        self.stdout.write(self.style.SUCCESS('****'))