from django.core.management.base import BaseCommand
from main.dump.move_data import main 
class Command(BaseCommand):
    help = 'This command is used to populate db with data.'

    def handle(self, *args, **options): 
        main() 
        self.stdout.write(self.style.SUCCESS('****'))