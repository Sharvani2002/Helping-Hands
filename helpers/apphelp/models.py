from django.db import models
from django.contrib.auth.models import User
import os
def get_image_path(instance, filename):
    return os.path.join('donation_pics', str(instance.id)+"_"+str(instance.points/10+1), filename)

class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    points = models.IntegerField(default =0)
    donation_pic = models.ImageField(upload_to=get_image_path, blank=True)

    def __str__(self):
        return self.user.username
