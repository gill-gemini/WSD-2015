from django.db import models

class Product(models.Model):
    """
    Write your model for the exercise 3 here. Remove the pass text.
    """
    title=models.CharField(max_length=255,blank=True, unique=True)
    description=models.TextField(blank=True)
    image_url=models.URLField(max_length=255,blank=True)
    quantity=models.BigIntegerField(blank=True,default=0)

    def sell(self):
        self.quantity = self.quantity - 1 #decrease the quantity by 1
        self.save() # make changes in the database
