import datetime


def today():
    today=datetime.datetime.now()
    return today.strftime('%d/%m/%Y, %H:%M')

def yesterday():
    oneDay=datetime.timedelta(days=1)
    today=datetime.datetime.now()
    yesterday=today-oneDay
    return yesterday.strftime('%d/%m/%Y, %H:%M')

def lastWeek():
    today=today=datetime.datetime.now()
    oneWeek=datetime.timedelta(weeks=1)
    lastWeek=today-oneWeek
    return lastWeek.strftime('%d/%m/%Y, %H:%M')



