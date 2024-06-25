from datetime import datetime, timedelta
from django.utils import timezone
from pytz import timezone as pytz_timezone 
def get_time_interval(period):
    # Get the timezone object for 'Asia/Kathmandu'
    asia_kathmandu_tz = pytz_timezone('Asia/Kathmandu')

    # Use timezone.localtime() with the correct timezone object
    now = timezone.localtime(timezone.now(), timezone=asia_kathmandu_tz)


    if period == "last_hour":
        end_time = (now).replace(minute=0, second=0, microsecond=0)
        start_time = end_time - timedelta(hours=1)
    elif period == "last_day":
        end_time = (now).replace(hour=0, minute=0, second=0, microsecond=0)
        start_time = end_time - timedelta(days=1)
    elif period == "last_week":
        end_of_last_week = now - timedelta(days=now.weekday() + 2)
        end_time = end_of_last_week.replace(hour=0, minute=0, second=0, microsecond=0)
        start_of_last_week = end_of_last_week - timedelta(days=6)
        start_time = start_of_last_week.replace(hour=0, minute=0, second=0, microsecond=0)

    elif period == "last_month":
        first_day_of_current_month = now.replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )
        last_day_of_last_month = first_day_of_current_month - timedelta(days=1)

        start_time = last_day_of_last_month.replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )
        end_time = last_day_of_last_month.replace(
            hour=23, minute=59, second=59, microsecond=999999
        )
    else:
        raise ValueError("Invalid time period")

    return start_time, end_time
