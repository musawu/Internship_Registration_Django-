from django.db import models


# Create your models here.

class Intern(models.Model):
    Intern_fname = models.CharField(max_length=30)
    Intern_lname = models.CharField(max_length=30)
    Intern_email = models.EmailField(unique=True)
    Intern_phoneNum = models.CharField(max_length=13, unique=True) 
    # Intern_profile_picture = CloudinaryField('image', default='https://example.com/default-image.jpg')
