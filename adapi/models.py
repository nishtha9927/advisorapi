from django.db import models

# Create your models here.
class advisordetail(models.Model):
    objects=models.manager
    name = models.CharField(max_length=100)
    imageurl = models.CharField(max_length=100)

class usermodel(models.Model):
    objects = models.manager
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class bookingdetail(models.Model):
    objects=models.manager
    advisor_id = models.ForeignKey(advisordetail,on_delete=models.CASCADE)
    booking_time = models.CharField(max_length=50)
    user_id = models.ForeignKey(usermodel,on_delete=models.CASCADE)





    
    
    
