import csv
from datetime import datetime
from itertools import islice
from django.conf import settings
from django.core.management.base import BaseCommand
from home.models import Book
from django.db import models
from decimal import Decimal

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%m/%d/%Y')
        return True
    except ValueError:
        return False

class Command(BaseCommand):
    help = 'Load book expenses from a csv file'


    def handle(self, *args, **kwargs):
        # Open the csv file
        csv_file_path = settings.BASE_DIR / 'data' / 'BooksDistributionExpenses.csv'
        
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                # Create a book instance
                book = Book()

                # Save the data from the csv to the book instance
                book.title = row['title']
                book.subtitle = row['subtitle']
                book.authors = row['authors']
                book.publisher = row['publisher']
            
                # Check if the published_date is valid before parsing
                if is_valid_date(row['published_date']):
                    book.published_date = datetime.strptime(row['published_date'], '%m/%d/%Y').date()
                else:
                    # print(f"Invalid date format for row: {row}")
                    continue  # Skip this row or handle it as needed
                
                book.category = row['category']
                book.distribution_expense = Decimal(row['distribution_expense'])
                if book.distribution_expense is not None and book.distribution_expense != '':
                    book.distribution_expense = Decimal(book.distribution_expense)
                else:
                    # Handle the case where distribution_expense is None or empty
                    # For example, you could set it to 0 or some other default value
                    book.distribution_expense = Decimal('0')
                            
                # Save the book to the database
                book.save()