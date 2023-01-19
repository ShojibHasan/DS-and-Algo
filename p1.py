# import csv
# file = open('/home/shojibhasan/Downloads/jxw-1000_url.csv')
# header = []
# for row in file:
#         header.append(row)
# print(header)


# print("____________________________________")

# file2 = open('/home/shojibhasan/Downloads/1000-url-summary - Sheet1.csv')

# header2 = []
# for row in file2:
#         header2.append(row)
        
# print(header2)


# from collections import OrderedDict
# from datetime import datetime, timedelta
# from dateutil.relativedelta import relativedelta

# startDate = '2016-1-28'
# endDate = '2017-3-26'

# start = datetime.strptime(startDate, '%Y-%m-%d').date()
# end = datetime.strptime(endDate, '%Y-%m-%d').date()

# while start < end:

    
#     start += relativedelta(months=1)
    
    
#     print(start)
#     start, end = [datetime.strptime(, "%Y-%m-%d") for  in [self.date_start, self.date_end]]
    
# a =list(OrderedDict(((start + timedelta(_)).strftime(r"%Y-%m"), None) for _ in ((end - start))).keys())

# print(a)

# import datetime
# from dateutil.rrule import rrule, MONTHLY

# strt_dt = datetime.date(2001,1,1)
# end_dt = datetime.date(2005,6,1)

# dates = [dt for dt in rrule(MONTHLY, dtstart=strt_dt, until=end_dt)]
# print(dates)
    
# from datetime import datetime

# date = '11-26-2021'
# print(datetime.strptime(date, "%m-%y"))

# # particulars_month_year =  str(month_last_date.month) + '.' + str(month_last_date.year)



# import calendar
# from datetime import datetime, timedelta


# def get_time_range_list(start_date, end_date):
#     date_range_list = []
#     while 1:
#         month_end = start_date.replace(day=calendar.monthrange(start_date.year, start_date.month)[1])
#         next_month_start = month_end + timedelta(days=1)
#         if next_month_start <= end_date:
#             date_range_list.append((start_date, month_end))
#             start_date = next_month_start
#         else:
#             date_range_list.append((start_date, end_date))
#             return date_range_list
        
# startDate = '2016-1-28'
# endDate = '2017-3-26'
# a = get_time_range_list(startDate,endDate)

# print(a)



# from datetime import timedelta, date

# def daterange(date1, date2):
#     for n in range(int ((date2 - date1).days)+1):
#         yield date1 + timedelta(n)

# start_dt = date(2015, 12, 20)
# end_dt = date(2016, 1, 11)
# for dt in q (start_dt, end_dt):
#     print(dt.strftime("%Y-%m-%d"))
    
    


# from datetime import date
# from dateutil.relativedelta import relativedelta

# sdate = date(2008, 8, 15)   # start date
# edate = date(2008, 9, 15)   # end date

# delta = edate - sdate       # as timedelta

# for i in range(delta.days + 1):
#     day = sdate + relativedelta(months=1)
#     print(day)



# from datetime import datetime, timedelta


# startDate = datetime(2020, 1, 10)
# endDate = datetime(2022, 4, 20)

# addDays = timedelta(days=31)

# while startDate <= endDate:
# 	print(startDate)
# 	startDate += addDays




# from datetime import datetime
# from dateutil import rrule


# start = datetime(2021, 1, 1)
# end = datetime(2022, 1, 1)

# for dt in rrule.rrule(rrule.MONTHLY, dtstart=start, until=end):
# 	print(dt)


# A,B,C = list(map(float,input().split()))
# print(max(A,B,C))
# traingle = 0.5*A*C
# circle = 3.14159*C*C
# trapizume = (A+B)/2.0*C
# square = B*B
# rectangle = A*B
# print("TRIANGULO: %.3lf"%traingle)
# print("CIRCULO: %.3f"%circle)
# print("TRAPEZIO: %.3f"%trapizume)
# print("QUADRADO: %.3f"%square)
# print("RETANGULO: %.3f"%rectangle)

import datetime

weekno = datetime.datetime.today().weekday()

if weekno < 5:
    print ("Weekday")
else:  # 5 Sat, 6 Sun
    print ("Weekend")
    
    
    
    