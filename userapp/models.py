from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=10)


class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=25)
    message = models.CharField(max_length=100)

class Attorneys(models.Model):
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=30)
    image = models.FileField(upload_to='image/')

class Client_Review(models.Model):
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    discription = models.CharField(max_length=100)
    image = models.FileField(upload_to='image/')

class Blog(models.Model):
    image = models.FileField(upload_to='image/')
    tittle = models.CharField(max_length=100)
    des = models.CharField(max_length=200)

class Types_Law(models.Model):
    law_tittle = models.CharField(max_length=50)
    point = models.CharField(max_length=150)
    detail = models.CharField(max_length=550)

class Practice_Area(models.Model):
    det = models.CharField(max_length=200)
    law_title = models.CharField(max_length=50)
    pid = models.ForeignKey(Types_Law,models.CASCADE)


class case_categories(models.Model):
    case_categories = models.CharField(max_length=50)
    
class case_studies(models.Model):
    case_studies_tittle = models.CharField(max_length=100)
    case_studies_tag = models.CharField(max_length=20)
    case_studies_date = models.CharField(max_length=20)
    case_studies_image = models.ImageField(upload_to='image/')