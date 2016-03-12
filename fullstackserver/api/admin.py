from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Link)
admin.site.register(UserSubscription)
admin.site.register(Cache)
admin.site.register(SubscriptionLink)