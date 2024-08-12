from django.db import models

# Create your models here.

class UserDetails(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=12, blank=True)
    
    def __str__(self) -> str:
        return self.username + " " + self.email  + " " + self.password
