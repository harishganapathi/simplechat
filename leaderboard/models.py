from django.db import models
from django.utils import timezone
from django.conf import settings 
# Create your models here.


class Scorecard(models.Model):
    serialNo = models.AutoField(primary_key = True)
    name = models.CharField(max_length=40)
    score = models.IntegerField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,default = 1)
 
    def publish(self):
        self.save()
   
    def __str__(self):
        return self.name




#class Signup(models.Model):
 #   fullName = models.CharField(max_length = 20)
  #  username = models.CharField(max_length= 25)
   # password = models.CharField(max_length = 12 , widget = forms.PasswordInput)
