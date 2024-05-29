from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'List all fields in User model'

    def handle(self, *args, **kwargs):
        for field in User._meta.get_fields():
            self.stdout.write(field.name)