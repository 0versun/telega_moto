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
    try:
        print('CHAT ID STORED', message.chat.id)
        store_id = message.chat.id
        data_processor.data_compressor(store_id)
    except:print('Something wrong')

def send_scheduled_message(ids):
    answer = bot_speach_examples.weather_string_generator_short()
    for items in ids:
        try:
            bot.send_message(items, answer, parse_mode='HTML')
        except:
            print('Yakas ebanina')

def send_bot_picture(ids, file_id):
    for items in ids:
        if int(items) < 0:
            try:
                bot.send_photo(items, photo=file_id)
                print (items,'Отправила')
            except:
                print('Фоточка по каким-то причинам не отправилась')

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
    try:
        print(40 * '-')
        print(datetime.now(), '\n')
        print(
            f'➡  Message from  {message.from_user.username} aka {message.from_user.first_name} {message.from_user.last_name} user_id = {str(message.from_user.id)} chat_id = {str(message.chat.id)} \n➡  Message = {message.text}'
        ) 
        print('\n', answer)
        print(40 * '_')
    except:print('Something wrong')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.reply_to(
            message,
            "Все путем мототело, используй слова 'бот прием' и 'бот куда едем' чтоб получить актуальную инфу по сабжу, жмякать старт каждый раз, не обязательно , а то жмякалка поломается."
        )
    except:print('Something wrong')

@bot.message_handler(commands=['short'])
def send_short_message(message):
    try:
        bot.send_chat_action(message.chat.id, action='typing')
        answer = bot_speach_examples.weather_string_generator_short()
        bot.reply_to(message, answer, parse_mode='HTML')
    except:print('Something wrong')

@bot.message_handler(commands=['long'])
def send_long_message(message):
    try:
        answer = bot_speach_examples.weather_string_generator_long()
        bot.reply_to(message, answer, parse_mode='HTML')
    except:print('Something wrong')

@bot.message_handler(commands=['radar'])
def send_radar_message(message):
    try:
        bot.send_chat_action(message.chat.id, action='upload_photo')
        link = weather_retreaver.weather_animation_retreaver()
        answer = f'<a href="{link}">окрыть оригинал</a>'
        bot.reply_to(message, answer, parse_mode='HTML')
    except:print('Something wrong')

@bot.message_handler(commands=['set_wake_up'])
def set_wake_up_time(message):
    sent = bot.send_message(message.chat.id, 'Когда просыпаться ?\n\
    укажи время в 24 форматном виде\n\
    например 10:40\n')
    bot.register_next_step_handler(sent, set_weak_up)

@bot.message_handler(commands=['set_pic'])
def set_pic(message):
    try:
        sent = bot.send_message(message.chat.id, 'скинь мне мою секси фотку и я ее запощу')
        bot.register_next_step_handler(sent, set_file_id)
    except:print('Something wrong')
    # print(message.photo.file_id)

def set_file_id(message):
    print('Пробую отослать файл')
    chat_ids = data_processor.return_stored_chat_id()
    # for items in chat_ids:
    try:
        file_id = message.photo[0].file_id
        # chat_ids = data_processor.return_stored_chat_id()
        send_bot_picture(chat_ids,file_id)
    except:print('Picture send wrong')

@bot.message_handler(commands=['say_something'])
def say_something(message):
    try:
        sent = bot.send_message(message.chat.id, 'Скажи что-то')
        bot.register_next_step_handler(sent, send_text)
    except:print('Somthg wrong')

def send_text(message):
    answer = message.text
    chat_ids = data_processor.return_stored_chat_id()
    try:
        for items in chat_ids:
            if int(items) < 0:
                try:
                    bot.send_message(items, answer, parse_mode='HTML')
                except: print('SMTHNGWRNG')
    except: print('Something wrong')

def set_weak_up(message):
    data_processor.data_write(data_tag='wake_up_time', value=message.text)
    bot.send_message(message.chat.id,
                            f"Поняла, буду просыпаться каждый день в {data_processor.data_read(data_tag='wake_up_time')}")


@bot.message_handler(commands=['set_destination'])
def send_welcome(message):
   if message.chat.id < 0:
       bot.send_message(message.chat.id, f"Пишите в личку {bot_speach_examples.welcome_word_processor()}.")
   else:
       try:    
           sent = bot.send_message(message.chat.id, 'Куда поедем ?')
           main_user = message.from_user.id
           bot.register_next_step_handler(sent, set_destination)
       except: print('Yakas ebanina happens')


def set_destination(message):
    try:
        user1 = {message.from_user.first_name: trip_storage.trip_attributes.append(message.text)}
        trip_storage.trip_storage.update(user1)
        sent = bot.send_message(message.chat.id,'а теперь время в цифрах, либо время суток')
        bot.register_next_step_handler(sent, set_time)
    except: print('Something went wrong')


def set_time(message):
    try:
        user1 = {message.from_user.first_name: trip_storage.trip_attributes.append(message.text)}
        trip_storage.trip_storage.update(user1)
        user_name = {message.from_user.first_name: trip_storage.trip_attributes.append(message.from_user.id)}
        trip_storage.trip_storage.update(user_name)
        bot.send_message(message.chat.id, 'Отлично, поняла!')
        trip_storage.trip_storage[message.from_user.first_name] = list(trip_storage.trip_attributes)
        trip_storage.trip_attributes.clear()
    except: print('Someting went wrong')


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
        try:
            answer = bot_speach_examples.weather_string_generator_short()
            console_output(message, answer)
            bot.reply_to(message, answer, parse_mode='HTML')
        except: print('Something wrong')

    elif str.lower(message.text) in (
            "бот, куда едем",
            "бот,куда едем",
            "бот ,куда едем",
            "бот , куда едем",
            "бот куда едем",
    ):

        if len(trip_storage.trip_storage) == 0:
            answer = 'Пока никто никуда не едет'
            try:
                bot.send_message(message.chat.id, answer, parse_mode='HTML' )
                console_output(message, answer)
            except: print('Something wrong')

        else:
            try:
                for keys in trip_storage.trip_storage:
                    answer = f'<a href="tg://user?id={trip_storage.trip_storage.get(keys)[2]}">{keys}</a> пердлагает ехать в {trip_storage.trip_storage.get(keys)[0]} ориентировочно {trip_storage.trip_storage.get(keys)[1]}'
                    bot.send_message(message.chat.id, answer, parse_mode='HTML')
                    console_output(message, answer)
            except: print('Something wrong')

    else:
        try:
            console_output(message, 'Message From Chat')
        except:print('Something wrong')

def bot_listener():
    bot.polling(none_stop=True, interval=1, timeout=50000)
