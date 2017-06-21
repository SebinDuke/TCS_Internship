from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=80,unique=True)
    auth_name = models.CharField(max_length=40)
    points = models.IntegerField(default=20)
    price = models.IntegerField(default=0)
    no_of_copies = models.IntegerField(default=0)
    #no_of_topics=models.IntegerField(default=0)
    #type_user=models.BooleanField()
    def __str__(self):
        return self.book_name