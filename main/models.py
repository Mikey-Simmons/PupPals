from django.db import models
import re 

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['dog_name']) < 3:
            errors['dog_name'] = "First name needs to be at least 3 characters"
        
        return errors
    def login_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 8:
            errors['email'] = "Email needs to be at least 8 characters"
        return errors
class User(models.Model):
    dog_name = models.CharField(max_length=50)
    dog_gender = models.CharField(max_length=50)
    dog_breed = models.CharField(max_length=50)
    dog_weight = models.IntegerField()
    dog_age = models.CharField(max_length=50)
    dog_city = models.CharField(max_length=50)
    dog_state = models.CharField(max_length=50)
    dog_owner_first = models.CharField(max_length=50)
    dog_owner_last = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()