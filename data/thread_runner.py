import _thread
import schedule
import time
import main_bot
from data import data_processor
from data import weather_retreaver

system = weather_retreaver.weather_formatter()
system.update_weather_data = 'Start'


def renew_weather_info():
    print('WEATHER UPDATED')
    system.update_weather_data = 'Start'


def send_time_message():
    main_bot.send_scheduled_message(data_processor.return_stored_chat_id())
    return print('TIME MASCHINE STARTED')


#def check_time():
#    time = data_processor.data_read(data_tag='wake_up_time')    
#    schedule.every().day.at(time).do(send_time_message)

schedule.every().day.at('08:00').do(send_time_message)
#schedule.every(1).minute.do(check_time)
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
    print('THREAD RUN error')
    time.sleep(2)
    flag = True
    raise Exception()
