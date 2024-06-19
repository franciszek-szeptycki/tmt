from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a user. Use --noinput to create a user johndoe with password password'

    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput',
            action='store_true',
            help='Create user johndoe with password password without any input',
        )
        parser.add_argument(
            '--username',
            type=str,
            help='Username for the user',
        )
        parser.add_argument(
            '--password',
            type=str,
            help='Password for the user',
        )

    def handle(self, *args, **options):
        if options['noinput']:
            username = 'johndoe'
            password = 'password'
        else:
            username = options.get('username')
            password = options.get('password')

            if not username or not password:
                self.stdout.write(self.style.ERROR('Username and password are required if --noinput is not specified'))
                return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f'User with username {username} already exists'))
        else:
            User.objects.create_user(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'User {username} created successfully'))
