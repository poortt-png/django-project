from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(username='admin')
        user.set_password('admin123')
        user.save()
        self.stdout.write('Password updated successfully')