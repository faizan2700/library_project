from django.core.management.base import BaseCommand
from main.dump.move_data import clean_data

class Command(BaseCommand):
    """
    Custom management command to truncate all data from the database.

    Usage:
        python manage.py clean_db
    """

    help = 'This command is used to truncate all data from the database.'

    def handle(self, *args, **options): 
        """
        Executes the command to truncate all data from the database.
        """
        clean_data() 
        self.stdout.write(self.style.SUCCESS('****'))