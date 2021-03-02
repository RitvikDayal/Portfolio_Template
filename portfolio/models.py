from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Visitor(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=500)
    message = models.TextField()
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name