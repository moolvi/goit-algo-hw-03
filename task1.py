from datetime import datetime

def get_days_from_today(date):
    try:
        format = '%Y-%m-%d'
        date_custom = datetime.strptime(date, format)
        now_date = datetime.today()
        return (now_date - date_custom).days
    except:
        return None