# data = [('Visa', 980.5), ('Rogers', 61.5), ('Visa', 215.0)]
# result = {}
# for card, value in data:
#         total = result.get(card, 0) + value
#         result[card] = total

    
# print (.)


# from datetime import date
# d0 = date(2020, 1, 1)
# d1 = date(2020, 4, 30+1)
# delta = d1 - d0
# print('The number of days between the given range of dates is :')
# print(delta.days)


# import datetime

# date1_str = '2022-12-15'
# date2_str = '2023-01-15'

# date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
# date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()

# delta =  (abs(date2-date1).days)+1

# print(delta)
      


import datetime

date_str = '2022-03-15'

date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

month_year_str = date.strftime('%m-%Y')

print(month_year_str)