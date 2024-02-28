def add_time(start, duration,day=""):
    [time,noon]=start.split(" ")
    [hours,min]=time.split(":")
    [hours_duration,min_duration]=duration.split(":")
    new_hours=(int(hours)+int(hours_duration))%12 +(int(min)+int(min_duration))//60
    new_min=(int(min)+int(min_duration))%60
    day_imp=""
    day_after=""
    number_day=int(hours_duration)//24
    hours_duration_resto=int(hours_duration)%24    
    if noon=="AM" and (int(hours)+int(hours_duration_resto)+(int(min)+int(min_duration))//60)//12>0:
        noon="PM"
    elif noon=="PM" and (int(hours)+int(hours_duration_resto)+(int(min)+int(min_duration))//60)//12>0:
        noon="AM"
        number_day=number_day+1
    if number_day==1:
        day_after="(next day)"
    elif number_day>1:
        day_after=f'({number_day} days later)'
    if not day=='':
        days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
        day=day.lower().split()
        day[0]=day[0].capitalize()
        day="".join(day)
        ind=days.index(day)
        new_ind=(ind+number_day)%7
        day_imp=f', {days[new_ind]}'
    return f'{str(new_hours)}:{str(new_min).rjust(2,"0")} {noon}{day_imp} {day_after}'.strip()
if __name__=="__main__":
    print(add_time("3:00 PM", "3:10"))
    print (add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))