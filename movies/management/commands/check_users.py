from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Check if admin user exists and list all users'

    def handle(self, *args, **options):
        users = User.objects.all()
        self.stdout.write('All users in database:')
        for user in users:
            self.stdout.write(f'- Username: {user.username}, ID: {user.id}, Is staff: {user.is_staff}')
        
        # Check if admin user exists
        try:
            admin_user = User.objects.get(username='admin')
            self.stdout.write(f'Admin user found: {admin_user.username}')
        except User.DoesNotExist:
            self.stdout.write('Admin user does not exist')