import json
import yaml
import requests
import arrow
import schedule
import time
import _thread

weather_params = yaml.load(open('credentials.yaml'))


def weather_url_constructor(params):
    # weather_params = yaml.load(open('credentials.yaml'))
    url_constructor = (weather_params['weather_url'] + params +
                       weather_params['weather_key_position'] +
                       weather_params['weather_api_token'] +
                       weather_params['city'])
    return url_constructor


def weather_current_retreaver(url=weather_url_constructor(weather_params['weather_now_prefix'])):
    weather_json_response = requests.get(url)
    return weather_json_response.text


def weather_forecast_retreaver(url=weather_url_constructor(weather_params['wether_forecast'])):
    weather_json_response = requests.get(url)
    return weather_json_response.text

print(arrow.utcnow().time())


def joba():
    print('106258322', 'OPAAAAAAAAAAAAAAAAAAAAAAAAA')
    # schedule.every().day.at('17:00').do(bot.send_message(message.chat.id, 'NEUJELI'))

schedule.every(1).minutes.do(joba)

def run_over():
    while True:

        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)

try:
    _thread.start_new_thread(run_over, ())
except:
    print('Ошибка')
    time.sleep(2)
    flag = True
    raise Exception()

