from django.core.management.base import BaseCommand
from main.dump.move_data import main 

class Command(BaseCommand):
    """
    Custom management command to populate the database with data.

    Usage:
        python manage.py populate_db
    """

    help = 'This command is used to populate the database with data.'

    def handle(self, *args, **options): 
        """
        Executes the command to populate the database.
        """
        main() 
        self.stdout.write(self.style.SUCCESS('****'))