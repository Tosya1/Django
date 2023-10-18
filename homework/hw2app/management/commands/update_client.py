from django.core.management.base import BaseCommand
from hw2app.models import Client

class Command(BaseCommand):
    help = "Update client name by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('tel', type=str, help='User tel')
        
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        tel = kwargs.get('tel')
        client = Client.objects.filter(pk=pk).first()
        client.tel_number = tel
        client.save()
        self.stdout.write(f'{client}')
