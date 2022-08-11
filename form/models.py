from django.db import models


class Signup(models.Model):
    full_name = models.CharField(max_length=9000)
    email = models.EmailField()
    payment_confirmed = models.BooleanField(default=False)
    signup_date = models.DateTimeField()


class Config(models.Model):
    spaces_available = models.PositiveBigIntegerField()
