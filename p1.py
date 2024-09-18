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

# import datetime

# weekno = datetime.datetime.today().weekday()

# if weekno < 5:
#     print ("Weekday")
# else:  # 5 Sat, 6 Sun
#     print ("Weekend")
    
    
import json   
import re
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

def sort_run_files(item):
    # Sort run files
    return [int(part) for part in item.split(".")[0].split('_') if part.isdigit()]

def filter_files_with_group_key(file_name_list, group_key):
    # Filter file names with group key
    return [file for file in file_name_list if re.search(group_key, file)]

def filter_files_with_file_keys(file_names, group_key, file_key_list):
    filtered_list = [
        file_name for file_name in file_names
        if any(file_key in file_name for file_key in file_key_list)
    ]
    # Extract group key dynamically using the provided pattern
    group_key_pattern = re.compile(f"(.*?{group_key})")

    # Group files based on the dynamically extracted group key
    data_list = {}
    for file in filtered_list:
        common_prefix_match = group_key_pattern.search(file)
        if common_prefix_match:
            common_prefix = common_prefix_match.group(1)
            if common_prefix not in data_list:
                data_list[common_prefix] = []
            data_list[common_prefix].append(file)

    # Filter groups that contain exactly the number of files in file_key_list
    group_data_list = {
        group_key: files for group_key, files in data_list.items()
        if len(files) == len(file_key_list)
    }

    # Sort the files within each group based on file_key_list order
    sorted_group_data_list = {}
    for group_key, group_data in group_data_list.items():
        sorted_group_data = sorted(
            group_data,
            key=lambda x: next((file_key for file_key in file_key_list if file_key in x), None)
        )
        sorted_group_data_list[group_key] = sorted_group_data
        
    return sorted_group_data_list


def extracted_file_names_list_with_run_file(file_name_list, group_key):
    # Extracted run files
    run_file_list = []
    for file in file_name_list:
        if len(file.split(".")) > 2 and file.split(".")[1].lower() == "run" and re.search(group_key, file):
            run_file_list.append(file)
        elif len(file.split(".")) <= 2 and file.split(".")[1].lower() == "run" and re.search(group_key, file):
            run_file_list.append(file)
    LOGGER.info('List of run files: {}'.format(run_file_list))
    
    # Sorted run files
    sorted_run_file_list = sorted(run_file_list, key=sort_run_files)
    LOGGER.info('Sorted list of run files: {}'.format(sorted_run_file_list))

    # Grouped files
    group_data_list = {}
    for run_file in sorted_run_file_list:
        # Extract the prefix up to the SKU, including everything before the group key and the group key itself
        match = re.search(group_key, run_file)
        if match:
            prefix = run_file[:match.end()]
            group_file_list = [file_item for file_item in file_name_list if file_item.startswith(prefix)]
            sorted_group_file_list = sorted(group_file_list)
            # Insert the run file into the sorted list
            sorted_group_file_list.append(run_file)
            sorted_group_file_list.pop(0)
            group_data_list[prefix] = sorted_group_file_list
    return group_data_list

def get_link_file_list(file_name_list, group_key, file_ready_flag, file_key_list=None):
    # 1. Input value check
    if not file_name_list:
        return {}
        
    if not isinstance(group_key, str) or group_key == "":
        LOGGER.error('No group key was specified.')
        raise Exception
        
    if not isinstance(file_ready_flag, bool):
        LOGGER.error('No run file flag was specified.')
        raise Exception
        
    if file_ready_flag is False:
        if not (isinstance(file_key_list, dict) and len(file_key_list["file_key_list"]) != 0 and isinstance(file_key_list["file_key_list"], list)):
            LOGGER.error('No file key list was specified.')
            raise Exception

    try:
        if file_ready_flag is False:
            # 2. RUN file flag is FALSE
            result = filter_files_with_file_keys(filter_files_with_group_key(file_name_list, group_key),group_key, file_key_list["file_key_list"])

            # 4. Return of acquisition results
            return result
        else:
            # 3. RUN file flag is TRUE
            result = extracted_file_names_list_with_run_file(file_name_list, group_key)

            # 4. Return of acquisition results
            return result
    except Exception as e:
        print(e)
        raise Exception

link_file_list = ['s3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-AAA-20240606.csv.20240916181607', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-AAA-20240606.csv.20240916181857', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-AAA-20240606.csv.20240916181625', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-AAA-20240606.csv.20240916181913', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-AAA-20240606.csv.20240916181630', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-AAA-20240606.csv.20240916181918', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-BBB-20240606.csv.20240916181954', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-BBB-20240606.csv.20240916182010', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-BBB-20240606.csv.20240916182015', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-CCC-20240606.csv.20240916182042', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-CCC-20240606.csv.20240916182059', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-CCC-20240606.csv.20240916182104']
processed_list = list(set([file.split('.csv')[0] + '.csv' for file in link_file_list]))


# link_file_list = ['s3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-AAA-20240606.csv.20240916160843', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-BBB-20240606.csv.20240916160859', 's3-sys-4-2/S3-SYS-4-1_50060_Sales_01_0001-CCC-20240606.csv.20240916160907']
group_keys = 'Sales_\d{2}_\d{4}'

outbound_file_ready_flag = False
file_key_lists = '{"file_key_list": ["AAA", "BBB", "CCC"]}'


print(get_link_file_list(processed_list,group_keys,outbound_file_ready_flag,json.loads(file_key_lists) if file_key_lists else None))