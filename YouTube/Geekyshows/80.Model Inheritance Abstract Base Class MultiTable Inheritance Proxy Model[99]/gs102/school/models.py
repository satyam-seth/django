from django.db import models

# Create your models here.

# class Student(models.Model):
#     name=models.CharField(max_length=70)
#     age=models.IntegerField()
#     fees=models.IntegerField()

# class Teacher(models.Model):
#     name=models.CharField(max_length=70)
#     age=models.IntegerField()
#     date=models.DateField()
#     salary=models.IntegerField()

# class Teacher(models.Model):
#     name=models.CharField(max_length=70)
#     age=models.IntegerField()
#     date=models.DateTimeField()
#     payment=models.IntegerField()

class CommanInfo(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True

class Student(CommanInfo):
    fees=models.IntegerField()
    date=None

class Teacher(CommanInfo):
    salary=models.IntegerField()

class Contractor(CommanInfo):
    date=models.DateTimeField()
    payment=models.IntegerField()