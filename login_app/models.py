from django.db import models

class User_info(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True) 
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.email
    
class UserSignUp(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.email   
    
class Wallpaper(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='wallpapers/') 
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title