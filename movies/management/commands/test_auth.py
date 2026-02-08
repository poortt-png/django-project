from django.core.management.base import BaseCommand
from django.contrib.auth import authenticate


class Command(BaseCommand):
    help = 'Test user authentication'

    def handle(self, *args, **options):
        # Test authenticating the admin user
        user = authenticate(username='admin', password='admin123')
        if user:
            self.stdout.write(f'Successfully authenticated user: {user.username}')
        else:
            self.stdout.write('Authentication failed for admin user')
            
        # Also test with the other user
        user2 = authenticate(username='timur', password='timur')  # assuming default password
        if user2:
            self.stdout.write(f'Successfully authenticated user: {user2.username}')
        else:
            self.stdout.write('Authentication failed for timur user')