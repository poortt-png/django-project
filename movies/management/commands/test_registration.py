from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Test registration by creating a test user'

    def handle(self, *args, **options):
        # Count users before
        count_before = User.objects.count()
        self.stdout.write(f'Users before test: {count_before}')
        
        # Try to create a test user
        try:
            test_user = User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123'
            )
            self.stdout.write(f'Test user created: {test_user.username}')
        except Exception as e:
            self.stdout.write(f'Error creating test user: {str(e)}')
        
        # Count users after
        count_after = User.objects.count()
        self.stdout.write(f'Users after test: {count_after}')
        
        # Try to authenticate the test user
        from django.contrib.auth import authenticate
        authenticated_user = authenticate(username='testuser', password='testpass123')
        if authenticated_user:
            self.stdout.write(f'Test user authenticated successfully: {authenticated_user.username}')
        else:
            self.stdout.write('Test user authentication failed')