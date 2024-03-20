from django.db import models


class Registration (models.Model):
    companyName=models.CharField(max_length=30)
    ownerName=models.CharField(max_length=20)
    rollNo=models.CharField(max_length=20)
    ownerEmail=models.EmailField()
    accessCode=models.CharField(max_length=20)

    # def __str__(self):
    #     return self.RollNumber

class Product(models.Model):
    productName=models.CharField(max_length=20)
    price=models.IntegerField()
    ratings=models.IntegerField()
    discount=models.IntegerField()
    availability=models.BooleanField(default=True)

    