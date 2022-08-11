from form.models import Config, Signup
from django.utils import timezone

def signup_user(
    email: str,
    full_name: str
):
    config = Config.objects.first()
    total_spaces_available = config.spaces_available

    Signup.objects.create(
        full_name=full_name,
        email=email,
        signup_date=timezone.now()
    )
    pass
