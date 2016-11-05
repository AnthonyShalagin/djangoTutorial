from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()


#If we reference post.title, it'll be an object
#We use the method below to convert it to a string 
    def __str__(self):
        return self.title
