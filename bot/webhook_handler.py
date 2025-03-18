from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import telebot
from leasing_app.models import LeasingRecord

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

def setup_commands():
    bot.set_my_commands([
        telebot.types.BotCommand('/start', 'Начало работы'),
        telebot.types.BotCommand('/update', 'Обновить данные'),
    ])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать! Доступные команды:\n"
        "/update - обновить данные\n"
        "/stats - статистика"
    )

@bot.message_handler(commands=['update'])
def handle_update(message):
    from django.core.management import call_command
    try:
        msg = bot.send_message(message.chat.id, "⏳ Начинаю обновление данных...")
        success = call_command('update_data')
        if success:
            bot.edit_message_text(
                "✅ Данные успешно обновлены!",
                chat_id=message.chat.id,
                message_id=msg.message_id
            )
        else:
            bot.edit_message_text(
                "❌ Ошибка при обновлении данных",
                chat_id=message.chat.id,
                message_id=msg.message_id
            )
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка: {str(e)}")
