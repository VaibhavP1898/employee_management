from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    date_of_joining = models.DateField()
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    address = models.TextField()
    leaves_taken = models.IntegerField(default=0)
    on_leave = models.BooleanField(default=False)

    def __str__(self):
        return self.name
