import telebot
import yaml

config = yaml.load(open('credentials.yaml'))
bot_token = config['token']

bot = telebot.TeleBot(bot_token)