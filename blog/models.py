from django.db import models

# Create your models here.
#title
#pub_date
#image
#body
#add blog app to settings
#create migrations
#add app to admin

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()