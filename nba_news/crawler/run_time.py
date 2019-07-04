import time
import datetime


def calculate_run_time(func):
    def wrapper():
        start_time = time.time()
        func()
        times = time.time() - start_time
        print(f'Execution Time: {datetime.timedelta(seconds=times)}')

    return wrapper