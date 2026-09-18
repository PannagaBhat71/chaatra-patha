from django.db import models

# Create your models here.

class student(models.Model):
    roll_number = models.IntegerField()
    student_name = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    age = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f"student {self.roll_number} - {self.student_name}"
    