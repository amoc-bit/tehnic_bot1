from django.core.management.base import BaseCommand
from django.conf import settings
import requests

class Command(BaseCommand):
    help = 'Set Telegram webhook'

    def handle(self, *args, **options):
        url = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/setWebhook'
        params = {'url': settings.WEBHOOK_URL}
        
        response = requests.post(url, data=params)
        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS('Webhook successfully set'))
        else:
            self.stderr.write(f'Error: {response.text}')
