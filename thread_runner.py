import _thread
import schedule
import time


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