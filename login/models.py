from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=80,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=120)
    pwd= models.CharField(max_length=32)
    points= models.IntegerField(default=0)
    #no_of_topics=models.IntegerField(default=0)
    #type_user=models.BooleanField()
    def __str__(self):
        return self.user_name
