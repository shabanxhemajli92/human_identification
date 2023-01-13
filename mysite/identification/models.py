from django.db import models

class Human(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    residency = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=100)
    payment_methods = models.CharField(max_length=100)
    cell_phone_provider = models.CharField(max_length=100)
    car_info = models.CharField(max_length=100)
    registration_plate = models.CharField(max_length=100)
    criminal_record = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
