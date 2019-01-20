import telebot
import yaml
from data import data_processor
from data import bot_speach_examples
from datetime import datetime

config = yaml.load(open('./data/settings/credentials.yaml'))
bot_token = config['token']

bot = telebot.TeleBot(bot_token)


def store_chat_id(message):
    print('CHAT ID STORED', message.chat.id)
    store_id = message.chat.id
    data_processor.data_compressor(store_id)


def send_scheduled_message(ids):
    answer = bot_speach_examples.weather_string_generator_short()
    for items in ids:
        bot.send_message(items, answer, parse_mode='HTML')


def console_output(message, answer):
    print(40 * '✅ ')
    print(datetime.now(), '\n')
    print(
        f'➡  Message from {message.from_user.first_name} {message.from_user.last_name} user_id = {str(message.from_user.id)} chat_id = {str(message.chat.id)} \n➡  Message = {message.text}'
    )
    print('\n', answer)
    print(40 * '✅ ')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Все путем мототело, используй слова 'бот прием' и 'бот куда едем' чтоб получить актуальную инфу по сабжу, жмякать старт каждый раз, не обязательно , а то жмякалка поломается."
    )


@bot.message_handler(commands=['short'])
def send_short_message(message):
    answer = bot_speach_examples.weather_string_generator_short()
    bot.reply_to(message, answer, parse_mode='HTML')


@bot.message_handler(commands=['long'])
def send_long_message(message):
    answer = bot_speach_examples.weather_string_generator_long()
    bot.reply_to(message, answer, parse_mode='HTML') 


@bot.message_handler(commands=['set_wake_up'])
def set_wake_up_time(message):
    sent = bot.send_message(message.chat.id, 'Когда просыпаться ?\n\
    укажи время в 24 форматном виде\n\
    например 10:40\n')
    bot.register_next_step_handler(sent, set_weak_up)


def set_weak_up(message):
    data_processor.data_write(data_tag='wake_up_time', value=message.text)
    bot.send_message(message.chat.id,
                            f"Понял, буду просыпаться каждый день в {data_processor.data_read(data_tag='wake_up_time')}")


@bot.message_handler(commands=['set_destination'])
def send_welcome(message):
    sent = bot.send_message(message.chat.id, 'Куда поедем ?')
    bot.register_next_step_handler(sent, set_destination)


def set_destination(message):
    data_processor.data_write(data_tag='destination', value=message.text)
    sent = bot.send_message(message.chat.id,
                            'а теперь время в цифрах, например 19:00')
    bot.register_next_step_handler(sent, set_time)


def set_time(message):
    data_processor.data_write(data_tag='destination_time', value=message.text)
    bot.send_message(message.chat.id, 'Спасибо')


@bot.message_handler(commands=['set_task'])
def send_welcome(message):
    sent = bot.send_message(message.chat.id,
                            'Какое событие будет отслеживать?')
    bot.register_next_step_handler(sent, set_year)


def set_year(message):
    data_processor.data_write(data_tag='seazon_reason', value=message.text)
    sent = bot.send_message(message.chat.id, 'Укажи цифрой год начала отсчета')
    bot.register_next_step_handler(sent, set_monunth)


def set_monunth(message):
    data_processor.data_write(data_tag='seazon_start_yaer', value=message.text)
    sent = bot.send_message(message.chat.id,
                            'Укажи цифрой месяц начала отсчета')
    bot.register_next_step_handler(sent, set_day)


def set_day(message):
    data_processor.data_write(
        data_tag='seazon_start_mounth', value=message.text)
    sent = bot.send_message(message.chat.id,
                            'Укажи цифрой день начала отсчета')
    bot.register_next_step_handler(sent, set_task)


def set_task(message):
    data_processor.data_write(data_tag='seazon_start_day', value=message.text)
    bot.send_message(message.chat.id, 'Занесено! Спи спокойно')


@bot.message_handler()
def handle_text(message):
    store_chat_id(message)
    if str.lower(message.text) in ("бот прием", "бот приём", "бот, прием",
                                   "ботприем", "ботприём", "бот,прием",
                                   "бот ,прием", "бот , прием"):
        answer = bot_speach_examples.weather_string_generator_short()
        console_output(message, answer)
        bot.reply_to(message, answer, parse_mode='HTML')

    elif str.lower(message.text) in (
            "бот, куда едем",
            "бот,куда едем",
            "бот ,куда едем",
            "бот , куда едем",
            "бот куда едем",
    ):
        answer = bot_speach_examples.where_to_go()
        console_output(message, answer)
        bot.reply_to(message, answer, parse_mode='HTML')

    else:
        console_output(message, 'Message From Chat')


def bot_listener():
    bot.polling(none_stop=True, interval=1, timeout=50000)
