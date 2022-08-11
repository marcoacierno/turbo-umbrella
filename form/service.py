from form.models import Config, Signup
from django.utils import timezone
from django.db import transaction
from django.core.mail import send_mail

def signup_user(
    email: str,
    full_name: str
):
    in_waiting_list = False
    # very stupid way to avoid over-selling?
    with transaction.atomic():
        config = Config.objects.select_for_update().first()
        total_spaces_available = config.spaces_available
        in_waiting_list = Signup.objects.count() >= total_spaces_available

    status = Signup.Status.PENDING_PAYMENT if not in_waiting_list else Signup.Status.WAITING_LIST

    signup = Signup.objects.create(
        full_name=full_name,
        email=email,
        signup_date=timezone.now(),
        status=status
    )

    # fail_silently ->
    # no background task so
    # in the thanks page a "email not arrived?" should cover this
    if signup.in_pending_payment:
        send_mail(
            'Thanks for your reservation! How to pay for X',
            config.email_with_payment_information,
            None,
            [signup.email],
            fail_silently=True,
        )
    elif signup.in_waiting_list:
        send_mail(
            'You are in the waiting list!',
            config.email_when_in_waiting_list,
            None,
            [signup.email],
            fail_silently=True,
        )
