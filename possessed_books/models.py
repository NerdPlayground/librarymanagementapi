from django.db import models
from datetime import date,timedelta

class PossessedBook(models.Model):
    book= models.OneToOneField('books.Book',related_name='possessedbook',on_delete=models.CASCADE)
    student= models.ForeignKey('patrons.Patron',related_name='possessedbooks',on_delete=models.CASCADE)
    due_date= date.today() + timedelta(days=5)
    return_delay_fine= models.IntegerField(default=0)