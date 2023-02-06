from dotenv import load_dotenv
import os
from sorts import find_ticker
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


updater = Updater(token=TELEGRAM_TOKEN)


def ticker_func(update, context):
    """Функция, которая обрабатывает поступающие текстовые сообщения"""
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    with open('id_new.csv', 'w') as f:
        f.write(str(chat.id))
        f.write('\n')
    phrase = update.message.text  # Вытаскиваем сообщение из бота
    for_user = find_ticker(phrase)  # Обрабатываем это сообщение
    context.bot.send_message(chat_id=chat.id, text=for_user)


def command_start(update, context):
    """Функция, которая обрабатывает поступающую команду start"""
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
                ['/start'],
                ['/help']
            ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=f'{format(name)}, введите тикер интересующей акции',
        reply_markup=buttons
    )


def command_help(update, context):
    """Функция, которая обрабатывает поступающие команды /help"""
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text=('Вот что я умею делать:\n'
              '1. Выводить текующую цену акции\n'
              '2. Выводить цену акции открытия\n'
              '3. Выводить общую рекомендацию по акции\n'
              'Необходимо ввести только тикер интересующей акции'),
    )


updater.dispatcher.add_handler(CommandHandler('start', command_start))
updater.dispatcher.add_handler(CommandHandler('help', command_help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, ticker_func))

# Метод start_polling() запускает процесс polling,
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling()
updater.idle()
