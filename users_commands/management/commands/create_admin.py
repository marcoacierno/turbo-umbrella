from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create admin'

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='admin@admin.it',
            username='admin',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('admin')
        user.save()
