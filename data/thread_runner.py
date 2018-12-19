import _thread
import schedule
import time
from data import weather_retreaver


def joba():
    print('106258322', 'OPAAAAAAAAAAAAAAAAAAAAAAAAA')
    # schedule.every().day.at('17:00').do(bot.send_message(message.chat.id, 'NEUJELI'))


schedule.every(1).minutes.do(joba)

system = weather_retreaver.weather_formatter()
system.update_weather_data = 'Start'

def renew_weather_info():
    print('WEATHER UPDATED')
    system.update_weather_data = 'Start'


schedule.every(1).hour.do(renew_weather_info)



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