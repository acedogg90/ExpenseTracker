from django.db import models

# Create your models here.
# models needed for "id", "title", "subtitle", "authors", "publisher", "published_date", "category", "distribution_expense"
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published_date = models.DateField(max_length=100)
    category = models.CharField(max_length=100)
    distribution_expense = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return(f"{self.title} {self.authors}")
    
    class Meta:
        ordering = ['published_date']