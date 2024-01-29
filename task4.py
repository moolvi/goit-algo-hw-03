from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    for user in users:
        try:
            now_date = datetime.today().date()
            date_custom = datetime(year = now_date.year, 
                                   month = datetime.strptime(user["birthday"], "%Y.%m.%d").month, 
                                   day = datetime.strptime(user["birthday"], "%Y.%m.%d").day).date()
            if (date_custom - now_date).days <= 7 and (date_custom - now_date).days >= 0:
                if date_custom.weekday() == 6:
                    user["birthday"] = (date_custom + timedelta(days = 1)).strftime("%Y.%m.%d")
                elif date_custom.weekday() == 5:
                    user["birthday"] = (date_custom + timedelta(days = 2)).strftime("%Y.%m.%d")
                else:
                    user["birthday"] = date_custom.strftime("%Y.%m.%d")
                upcoming_birthdays.append(user)
        except:
            return None
    return upcoming_birthdays