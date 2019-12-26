import telebot
import yaml
from data import data_processor
from data import bot_speach_examples
from data import trip_storage
from data import weather_retreaver
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
        try:
            bot.send_message(items, answer, parse_mode='HTML')
        except:
            print('Yakas ebanina')

def send_scheduled_animation(ids):
    answer = bot_speach_examples.weather_animation_generator()
    for items in ids:
        try:
            bot.send_message(items, answer, parse_mode='HTML')
        except:
            print('Yakas HUITA')


def send_scheduled_weather_animation(ids):
    answer = bot_speach_examples.weather_string_generator_short()
    for items in ids:
        try:
            bot.send_message(items, answer, parse_mode='HTML')
        except:
            print('Yakas ebanina')    

def console_output(message, answer):
    print(40 * '✅ ')
    print(datetime.now(), '\n')
    print(
        f'➡  Message from  {message.from_user.username} aka {message.from_user.first_name} {message.from_user.last_name} user_id = {str(message.from_user.id)} chat_id = {str(message.chat.id)} \n➡  Message = {message.text}'
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
    bot.send_chat_action(message.chat.id, action='typing')
    answer = bot_speach_examples.weather_string_generator_short()
    bot.reply_to(message, answer, parse_mode='HTML')


@bot.message_handler(commands=['long'])
def send_long_message(message):
    answer = bot_speach_examples.weather_string_generator_long()
    bot.reply_to(message, answer, parse_mode='HTML')

@bot.message_handler(commands=['radar'])
def send_radar_message(message):
    bot.send_chat_action(message.chat.id, action='upload_photo')
    link = weather_retreaver.weather_animation_retreaver()
    answer = f'<a href="{link}">окрыть оригинал</a>'
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


#@bot.message_handler(commands=['set_destination'])
#def send_welcome(message):
#    sent = bot.send_message(message.chat.id, 'Куда поедем ?')
#    bot.register_next_step_handler(sent, set_destination)


#def set_destination(message):
#    user1 = {message.from_user.first_name: trip_storage.trip_attributes.append(message.text)}
#    trip_storage.trip_storage.update(user1)
#    sent = bot.send_message(message.chat.id,'а теперь время в цифрах, либо время суток')
#    bot.register_next_step_handler(sent, set_time)


def set_time(message):
    user1 = {message.from_user.first_name: trip_storage.trip_attributes.append(message.text)}
    trip_storage.trip_storage.update(user1)
    user_name = {message.from_user.first_name: trip_storage.trip_attributes.append(message.from_user.id)}
    trip_storage.trip_storage.update(user_name)
    bot.send_message(message.chat.id, 'Отлично, принято!')
    trip_storage.trip_storage[message.from_user.first_name] = list(trip_storage.trip_attributes)
    trip_storage.trip_attributes.clear()


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

        if len(trip_storage.trip_storage) == 0:
            answer = 'Пока никто никуда не едет'
            bot.send_message(message.chat.id, answer, parse_mode='HTML' )
            console_output(message, answer)

        else:
            for keys in trip_storage.trip_storage:
                answer = f'<a href="tg://user?id={trip_storage.trip_storage.get(keys)[2]}">{keys}</a> пердлагает ехать в {trip_storage.trip_storage.get(keys)[0]} ориентировочно {trip_storage.trip_storage.get(keys)[1]}'
                bot.send_message(message.chat.id, answer, parse_mode='HTML')
                console_output(message, answer)

    else:
        console_output(message, 'Message From Chat')


def bot_listener():
    bot.polling(none_stop=True, interval=1, timeout=50000)
