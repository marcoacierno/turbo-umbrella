from django.db import models


class Signup(models.Model):
    class Status(models.TextChoices):
        PENDING_PAYMENT = 'pending', 'Waiting Payment'
        PAYMENT_CONFIRMED = 'confirmed', 'Payment confirmed'
        WAITING_LIST = 'waiting_list', 'Waiting list'

    full_name = models.CharField(max_length=9000)
    email = models.EmailField()
    signup_date = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        choices=Status.choices,
    )

    def in_waiting_list(self) -> bool:
        return self.status == Signup.Status.WAITING_LIST

    def in_pending_payment(self) -> bool:
        return self.status == Signup.Status.PENDING_PAYMENT


class Config(models.Model):
    spaces_available = models.PositiveBigIntegerField()

    email_with_payment_information = models.TextField(blank=True, default='')
    email_when_in_waiting_list = models.TextField(blank=True, default='')
