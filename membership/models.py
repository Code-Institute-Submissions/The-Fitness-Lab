from django.db import models

from accounts.models import UserAccount
import datetime


# Create your models here.


class Membership(models.Model):
    """
    Model for membership
    """
    MEMBERSHIP_CHOICES = [
        ('monthly', ('Monthly')),
        ('annually', ('Annually')),
    ]

    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES, default='monthly',
        max_length=30
    )
    price = models.IntegerField(null=True)
    duration_days = models.IntegerField(null=True)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    """
    Model for user profile membeship
    """
    member_profile = models.ForeignKey(UserAccount, on_delete=models.SET_NULL,
                                       null=True, blank=False,
                                       related_name='member')
    user_membership = models.ForeignKey(
        Membership, related_name='user_membership', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.member_profile.name


class Subscription(models.Model):
    """
    Model for Subsciption
    """
    subcription_membership = models.ForeignKey(
        UserMembership, related_name='subscription', on_delete=models.CASCADE)
    membership_duration = models.ForeignKey(
        Membership, related_name='duration', on_delete=models.CASCADE)
    purchase_date = models.DateField(null=True, default=datetime.date.today)
    expiration_date = models.DateField(null=True, default=datetime.date.today)
    active = models.BooleanField(default=True)
    cancelled = models.BooleanField(default=True)

    def set_expiration_date(self):
        self.expiration_date = self.purchase_date + \
            datetime.timedelta(days=self.membership_duration.duration_days)

    def save(self, *args, **kwargs):
        self.set_expiration_date()
        # Call the save method as defined in the superclass i.e. models.Model
        super().save(*args, **kwargs)
