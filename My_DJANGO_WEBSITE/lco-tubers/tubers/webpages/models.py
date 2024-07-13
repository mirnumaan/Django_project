from django.db import models 



# creating my admin panel properties


class  Slider(models.Model):

    headline= models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    button_text=models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
   

    def  __str__(self):
        return self.headline

class Group(models.Model):
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    fb_id=models.CharField(max_length=255)
    insta_id=models.CharField(max_length=255)
    yt_id=models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y/')
  

    def __str__(self):
        return self.first_name





