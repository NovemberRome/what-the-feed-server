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
        return 'username ' + self.username + ' with id ' + str(self.id)


class Link(models.Model):
    pid = models.AutoField(primary_key=True)
    url = models.TextField()
    network = models.CharField(max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Network ' + self.network + ' - ' + self.name


class UserSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    searchParam = models.CharField(max_length=100)

    def __str__(self):
        return 'Subscription for ' + self.searchParam + ' by user ' + self.user.username + ' subid ' + str(self.id)


class SubscriptionLink(models.Model):
    userSub = models.ForeignKey(UserSubscription, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)

    def __str__(self):
        return 'Subscription' + str(self.userSub.id) + ' ' + self.link.network + ' ' + self.link.name


class Cache(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    data = models.TextField()
    expiry = models.CharField(max_length=40)

    def __str__(self):
        return 'Cache for ' + self.link.network + ' ' + self.link.name