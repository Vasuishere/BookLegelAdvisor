from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=25)
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Attorneys(models.Model):
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=30)
    image = models.FileField(upload_to='image/')
    def __str__(self):
        return self.name
    

class Client_Review(models.Model):
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    discription = models.CharField(max_length=100)
    image = models.FileField(upload_to='image/')
    def __str__(self):
        return self.name

class Blog(models.Model):
    image = models.FileField(upload_to='image/')
    tittle = models.CharField(max_length=100)
    des = models.CharField(max_length=1500)
    def __str__(self):
        return self.tittle

class Types_Law(models.Model):
    law_tittle = models.CharField(max_length=50)
    point = models.CharField(max_length=150)
    detail = models.CharField(max_length=550)
    def __str__(self):
        return self.law_tittle

class Practice_Area(models.Model):
    Practice_Area_det = models.CharField(max_length=1000)
    Practice_Area_law_title = models.CharField(max_length=50)
    Practice_Area_pid = models.ForeignKey(Types_Law,models.CASCADE)
    Practice_Area_image = models.ImageField(upload_to='image/')
    

class case_categories(models.Model):
    case_categories = models.CharField(max_length=50)
    def __str__(self):
        return self.case_categories
    
class case_studies(models.Model):
    case_studies_tittle = models.CharField(max_length=100)
    case_studies_tag = models.CharField(max_length=20)
    case_studies_date = models.CharField(max_length=20)
    case_studies_image = models.ImageField(upload_to='image/')
    def __str__(self):
        return self.case_studies_tittle