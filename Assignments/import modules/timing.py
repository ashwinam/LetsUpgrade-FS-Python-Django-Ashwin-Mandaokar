import time,calendar

def e_h(t1):
    t9 = time.localtime(t1)
    print(t9)
    # format for printing 25-10-2021 14:10:45
    d1 = time.strftime("%d-%m-%Y %H:%M:%S", t9)
    d2 = time.strftime("%d-%m-%Y %r", t9)
    print(d2)
    return d1


print(e_h(1629022256))

date1 = "15 Aug 2021 10:10:56"

def h_e(date1):
    t9 = time.strptime(date1, "%d %b %Y %H:%M:%S")
    t1 = time.mktime(t9)
    t2 = calendar.timegm(t9)
    return t1,t2

print(h_e(date1))