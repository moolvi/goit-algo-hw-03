from datetime import datetime

def get_days_from_today(date):
    format = '%Y-%m-%d'
    date_custom = datetime.strptime(date, format).today()
    now_date = datetime.now().today()
    return (now_date - date_custom).days()