from django.db import models
from datetime import datetime

# Create your models here.
class Youtuber(models.Model):

    crew_choices=(
        ('solo' , 'solo'),
        ('small','small'),
        ('large' , 'large')
    )

    camera_choices=(
        ('canon' , 'canon'),
        ('nikon','nikon'),
        ('sony' , 'sony'),
        ('red' , 'red'),
        ('fuji','fuji'),
        ('panasonic' , 'panasonic'),
        ('other' , 'other')
    
    )
    category_choices=(
        ('code' , 'code'),
        ('mobile_review','mobile_review'),
        ('vlogs' , 'vlogs'),
        ('comedy' , 'comedy'),
        ('gaming','gaming'),
        ('flim_makinhg' , 'film_making'),
        ('cooking' , 'cooking')
    
    )
    # def data():
    #     [
    #     'crew_choices':'crew_choices',
    #     'camera_choices':'camera_choices'
    #     ]


    name= models.CharField(max_length= 255)
    
    
    photo= models.ImageField(upload_to = 'media/ytubers/%Y/%m')
    video_url = models.CharField(max_length= 255)
    description = models.CharField(max_length=255)
    city = models.CharField(max_length= 255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices,max_length= 255)
    camera_type = models.CharField(choices=camera_choices,max_length=255)
    sub_count = models.CharField(max_length=255)
    category = models.CharField(choices=category_choices,max_length= 255)
    is_featured = models.BooleanField(default= False)
    created_date= models.DateTimeField(default=datetime.now, blank= True)

    def __str__(self):
        return self.first_name
