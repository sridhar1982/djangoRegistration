from django.db import models
from registration.models import User
from registration.signals import user_registered

class ExUserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    ishuman = models.BooleanField(required=True)
    dateofBirth=models.DateField(required=True)
 
    def __unicode__(self):
        return self.user


def user_registered_callback(sender, user, request, **kwargs):
    profile = ExUserProfile(user = user)
    profile.ishuman = bool(request.POST["ishuman"])
    profile.dateofBirth=request.POST["dateofBirth"]
    print request.POST["dateofBirth"]
    profile.save()
 
user_registered.connect(user_registered_callback)
