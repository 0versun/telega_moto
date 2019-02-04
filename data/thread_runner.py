import threading
import schedule
import time
import main_bot
from data import data_processor
from data import weather_retreaver
from data import trip_storage

system = weather_retreaver.weather_formatter()
system.update_weather_data = 'Start'


def renew_weather_info():
    print('WEATHER UPDATED')
    system.update_weather_data = 'Start'


def send_time_message():
    main_bot.send_scheduled_message(data_processor.return_stored_chat_id())
    return print('TIME MASCHINE STARTED')


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def reset_trips():
    trip_storage.trip_storage.clear()

def runschedule():

    schedule.every().day.at('08:00').do(run_threaded, send_time_message)
    schedule.every(1).hour.do(run_threaded, renew_weather_info)
    schedule.every().day.at('00:00').do(run_threaded, reset_trips)
    while 1:
            schedule.run_pending()
            time.sleep(1)

