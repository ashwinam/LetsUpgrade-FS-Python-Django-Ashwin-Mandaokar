import datetime
import pytz

country_names= input("Enter the cuntry name :").lower()

for ab,cn in pytz.country_names.items():
    if country_names == cn.lower():
        ab_name = ab
        print("Abriviation ",ab_name)
        break
    

if ab_name:
    allTimeZones = list(pytz.country_timezones.get(ab_name))
    allignment_text = len(max(allTimeZones,key = len))+1
    for each in allTimeZones:
        print(each.ljust(allignment_text,"*"),"\t",datetime.datetime.now(pytz.timezone(each)))