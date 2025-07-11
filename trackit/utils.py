from datetime import date, datetime, timedelta
import calendar
import time

now = datetime.now()
today = date.today()
day = today.day
year = today.year
month = today.month
week_indx = today.weekday()

next_hour = (now + timedelta(hours=1)).replace(minute=0,
                                               second=0, microsecond=0)




next_day = (now + timedelta(days=1)
            ).replace(hour=0, minute=0, second=0)
next_week = 6 - week_indx
month_range = calendar.monthrange(year, month)[1]
last_day = date(year, 12, 31)
week_days_left = (last_day - today).days

    # Countdown
def countdown(value, root):
    if root == "minutes(s)":
        while value:
            mins, secs = divmod(value, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            print(time_format, end="\r")  # \r overwrites the same line
            time.sleep(1)
            value -= 1

        print("Time's up!")

