import datetime


def today():
    today=datetime.datetime.now()
    return today

def yesterday():
    oneDay=datetime.timedelta(days=1)
    today=datetime.datetime.now()
    return today-oneDay

def lastWeek():
    today=today=datetime.datetime.now()
    oneWeek=datetime.timedelta(weeks=1)
    return today-oneWeek

