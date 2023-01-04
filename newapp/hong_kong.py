import pytz
from datetime import datetime


def convert_utc_to_hong_kong(utc_time):
    hong_kong_tz = pytz.timezone('Asia/Hong_Kong')

    utc_time_dt = datetime.utcfromtimestamp(utc_time)

    hong_kong_time_dt = utc_time_dt.replace(
        tzinfo=pytz.utc).astimezone(hong_kong_tz)

    return hong_kong_time_dt.strftime('%Y-%m-%d %H:%M:%S')


utc_time = 024532.465224  # 2021-01-01 00:00:00 UTC
hong_kong_time = convert_utc_to_hong_kong(utc_time)
print(hong_kong_time)


def convert_utc_to_hong_kong(utc_time):
    # Set the timezone for Hong Kong
    hong_kong_tz = pytz.timezone('Asia/Hong_Kong')

    # Convert the UTC time to a datetime object
    utc_time_dt = datetime.utcfromtimestamp(utc_time)

    # Set the datetime object to be in the Hong Kong timezone
    hong_kong_time_dt = utc_time_dt.replace(
        tzinfo=pytz.utc).astimezone(hong_kong_tz)

    # Calculate the difference between the current time and the Hong Kong time
    time_difference = datetime.now(hong_kong_tz) - hong_kong_time_dt

    # Return the number of hours ago the time in Hong Kong occurred
    return time_difference.total_seconds() / 3600


utc_time = 20230103024532.465224  # 2021-01-01 00:00:00 UTC
hours_ago = convert_utc_to_hong_kong(utc_time)
print(hours_ago)
