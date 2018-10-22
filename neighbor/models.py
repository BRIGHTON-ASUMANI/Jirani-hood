from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime as dt
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.utils import timezone

from django.core.urlresolvers import reverse

class Neighbourhood(models.Model):
    user = models.ForeignKey(User, related_name="poster", on_delete=models.CASCADE)
    neighbourhood_location = models.CharField(max_length=40)
    neighbourhood_name = models.CharField(max_length=40)
    occupants_count = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse('dump', kwargs={'pk':self.pk})


    @classmethod
    def get_all(cls):
        neighbourhood = Neighbourhood.objects.all()
        return neighbourhood

    @classmethod
    def save_neighbourhood(self):
        return self.save()

    @classmethod
    def delete_neighbourhood(self):
        return self.delete()

    def __str__(self):
        return self.neighbourhood_name



class Profile(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name="poster", on_delete=models.CASCADE)
    picture = ImageField(manual_crop='')
    user_email = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('dump', kwargs={'pk':self.pk})

    @classmethod
    def get_all(cls):
        profiles = Profile.objects.all()
        return profiles

    @classmethod
    def save_profile(self):
        return self.save()

    @classmethod
    def delete_profile(self):
        return self.delete()

    def __str__(self):
        return self.user.username


class Business(models.Model):
    user = models.ForeignKey(User, related_name="business_user", on_delete=models.CASCADE)
    business_name = models.CharField(max_length=40, blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name="neighbor", on_delete=models.CASCADE)
    business_email = models.EmailField()

    def get_absolute_url(self):
        return reverse('dump', kwargs={'pk':self.pk})


    def __str__(self):
        return self.business_name

    @classmethod
    def all_business(cls):
        business = cls.objects.order_by('business_name')
        return business


    @classmethod
    def get_business(cls, id):
        business = cls.objects.get(id=id)
        return business
