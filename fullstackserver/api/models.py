from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(null=False, max_length=100)
    username = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)

    def __str__(self):
        return 'User ' + self.username + ' and ID ' + str(self.id)


class Link(models.Model):
    pid = models.AutoField(primary_key=True)
    link = models.TextField()
    network = models.IntegerField()


class SearchString(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    query = models.CharField(max_length=100)


class Cache(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    data = models.TextField()
    expiry = models.DateTimeField()
