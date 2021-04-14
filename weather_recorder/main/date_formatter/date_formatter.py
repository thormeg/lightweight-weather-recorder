"""Date formatting utility."""
from datetime import datetime

def format_date(date: str) -> datetime:
    return datetime.strptime(
            date + ' 00:00:00.000001'
            , '%Y-%m-%d %H:%M:%S.%f')
