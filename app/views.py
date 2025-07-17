# ver1.0.0 не загружено

import json
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .async_bot import bot
from telebot.util import Update
import logging
# ver 1.0.0 не загружено
# логирование django
logger = logging.getLogger(__name__)  #

logger.info(f'the module {__name__} running')

@csrf_exempt
async def telegram_webhook(request):
    try:
        if request.method == 'POST':
            # Проверка секретного токена (опционально)  - разобраться
            if request.headers.get('X-Telegram-Bot-Api-Secret-Token') != settings.TELEGRAM_WEBHOOK_SECRET:
                # return HttpResponseForbidden("Invalid token")
                logger.info(f'the secret key in telegram request {__name__} incorrect')


            # Асинхронная обработка
            update_json = json.loads(await request.aread())
            update = Update.de_json(update_json)
            await bot.process_new_updates([update])
            return HttpResponse("OK")
            logger.info(f'{__name__} OK')

        return HttpResponse("Only POST allowed")
        logger.info(f'{__name__} incorrect request.method. Only POST allowed')

    except Exception as e:

        logger.error(f"Error checking subscription: {e}")
        # print(f"Error checking subscription: {e}")
        return False
