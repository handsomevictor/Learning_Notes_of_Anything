# The following codes only help you find if there are empty slots in 3 stations near
# Cergy, the three stations are goussainville, stade, and SDIS 60 (first one most preferred).

import time
from datetime import timedelta, date
from check_functions import check_today, check_tomorrow, check_next_week

if __name__ == '__main__':

    localtime = time.localtime(time.time())

    today = str(localtime.tm_year) + '-' + str(localtime.tm_mon) + '-' + str(localtime.tm_mday)
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    next_week = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")

    check_today(today)
    check_tomorrow(tomorrow)
    check_next_week(next_week)

    count = 0
    b = 10
    print('after 10 seconds, this window will be closed.')

    while (count < b):
        ncount = b - count
        print(ncount, ' seconds left')
        time.sleep(1)
        count += 1

    print('bye bye!')
    time.sleep(1)