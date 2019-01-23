import main_bot
from data import thread_runner
import threading
'''Run bot on instance'''


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


run_threaded(main_bot.bot_listener)
run_threaded(thread_runner.runschedule)