from django.db import models
from login.models import User
def rand_key(size):
    return ''.join([random.choice(string.letters + string.digits) for i in range(size)])


class Books(models.Model):
    book_name = models.CharField(max_length=80,unique=True)
    auth_name = models.CharField(max_length=40)
    points = models.IntegerField(default=20)
    price = models.IntegerField(default=0)
    no_of_copies = models.IntegerField(default=0)
    varification = models.BooleanField(default=False)
    #no_of_topics=models.IntegerField(default=0)
    #type_user=models.BooleanField()
    def __str__(self):
        return self.book_name

class Order(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    delivered=models.BooleanField(default=False)
    address = models.CharField(max_length=200)

    def __str__(self):
        aii=str(self.auto_increment_id)
        return aii
