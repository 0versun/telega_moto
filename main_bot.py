import telebot
import yaml
from data import thread_runner
from data import bot_speach_examples
from datetime import datetime

config = yaml.load(open('./data/settings/credentials.yaml'))
bot_token = config['token']

bot = telebot.TeleBot(bot_token)


def console_output(message, answer):
    print(40 * '✅ ')
    print(datetime.now(), '\n')
    print(
        f'➡  Message from {message.from_user.first_name} {message.from_user.last_name} user_id = {str(message.from_user.id)} chat_id = {str(message.chat.id)} \n➡  Message = {message.text}'
    )
    print('\n', answer)
    print(40 * '✅ ')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler()
def handle_text(message):
    answer = bot_speach_examples.weather_string_generator()

    if str.lower(message.text) == "pogoda":
        console_output(message, answer)
        bot.reply_to(message, answer, parse_mode='HTML')
    elif str.lower(message.text) == "kek dela":
        answer = 'TRIGGEREEEDDDD'
        console_output(message, answer)
        bot.reply_to(message, answer)
    else:
        console_output(message, 'Message From Chat')


bot.polling(none_stop=True, interval=1, timeout=50000)
