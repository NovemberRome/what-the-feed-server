from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField()
    username = models.CharField(max_length=20)
    email = models.EmailField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)

    def __str__(self):
        return 'User ' + self.username + ' and ID ' + self.id


class Link(models.Model):
    pid = models.AutoField(primary_key=True)
    link = models.CharField()
    network = models.IntegerField()


class SearchString(models.Model):
    id = models.ForeignKey(User, on_delete='cascade')
    pid = models.ForeignKey(Link, on_delete='cascade')
    query = models.CharField()


class Cache(models.Model):
    pid = models.ForeignKey(Link, on_delete='cascade')
    data = models.TextField()
    expiry = models.DateTimeField()
