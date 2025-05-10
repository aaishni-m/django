from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    phno = models.IntegerField()
    percentage = models.IntegerField()

    def __str__(self):
        return f"name: {self.name} \nphone number: {self.phno}\n percentage: {self.percentage}" 