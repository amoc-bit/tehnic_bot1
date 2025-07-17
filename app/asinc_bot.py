import logging
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
from .models import TelegramUser

# ver1.0.0 не осмыслено только копия

logger = logging.getLogger(__name__)
bot = AsyncTeleBot(settings.TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
async def handle_start(message):
    try:
        user = message.from_user
        await TelegramUser.objects.aupdate_or_create(
            user_id=user.id,
            defaults={
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        )
        await bot.reply_to(message, "✅ Вы зарегистрированы!")
    except Exception as e:
        logger.error(f"Error in handle_start: {e}")
        await bot.reply_to(message, "⚠️ Произошла ошибка")

@bot.message_handler(func=lambda message: True)
async def echo_all(message):
    await bot.reply_to(message, f"Эхо: {message.text}")
