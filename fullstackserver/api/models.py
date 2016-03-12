from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=30, null=True)
    lastName = models.CharField(max_length=30, null=True)

    def __str__(self):
        return 'User ' + self.username + ' and ID ' + str(self.id)


class Link(models.Model):
    pid = models.AutoField(primary_key=True)
    link = models.TextField()
    network = models.IntegerField()
    name = models.CharField(max_length=50)


class UserSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=100)


class SubscriptionLink(models.Model):
    userSub = models.ForeignKey(UserSubscription, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)


class Cache(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    data = models.TextField()
    expiry = models.DateTimeField()
