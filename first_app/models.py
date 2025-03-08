from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self):
        return f"Name: {self.name}"

# Model Inheritance
# 1. abstract base class
# 2. multitable inheritance
# 3. proxy model

# 1. abstract base class
class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    class Meta:
        abstract = True

class StudentInfoModel(CommonInfo):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=20)
    
class TeacherInfoModel(CommonInfo):
    salary = models.IntegerField()