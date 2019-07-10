from django.db import models

class EmployeeDetails(models.Model):
    name  = models.CharField(max_length=100) 
    photo =models.ImageField(upload_to='Photos/')
    email = models.EmailField(max_length=30)
    mobile = models.PositiveIntegerField(max_length=13)
    designation = models.CharField(max_length=50)
    skills = models.TextField(max_length=500)
    about = models.TextField(max_length=500)
    resume=models.FileField(upload_to='Resume/')

    def __str__(self):
        return self.name

