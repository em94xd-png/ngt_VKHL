from datetime import date, timedelta

def format1_today():
    today = date.today()
    return today.strftime("%d%m")

print(format1_today())