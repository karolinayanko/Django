#!/usr/bin/python
# -*- coding: utf-8 -*-
import re, os, sys
#processor of string date to digits
#receives dd-str_of_month-yyyy or (better) yyyy-str_of_month-dd
#returns dd-mm-yyyy or yyyy-mm-dd
def date_processor(date):
    filtered_date = date
    dates_dict = {
        'янв':'01',
        'фев':'02',
        'мар':'03',
        'апр':'04',
        'май':'05',
        'мая':'05',
        'июн':'06',
        'июл':'07',
        'авг':'08',
        'сен':'09',
        'окт':'10',
        'ноя':'11',
        'дек':'12',
    }
    for month in dates_dict:
        if month.decode('utf-8') in date.decode('utf-8').lower():
            # print month.decode('utf-8'), "=", date.decode('utf-8').lower()
            #replacing srting month to month number
            filtered_date = re.sub(r'(.*?)\..*?\.(.*)',r'\1.=_=.\2',date.decode('utf-8').lower().replace('-','.').replace(' ','.'))
            filtered_date = filtered_date.replace('=_=', dates_dict[month]).replace('.','-')
            #searching days - if we have a day "1" and not "01" - adding zero
            filtered_date = re.sub(r'^(\d{1}\D.*)',r'0\1',filtered_date)
            filtered_date = re.sub(r'(.*\D)(\d{1})$',r'\1zero\2',filtered_date).replace('zero','0')
    return filtered_date
# print date_processor('9-Дек-07')
# print date_processor('17 мая 2013')
# print date_processor('23.Янв.2011')
# print date_processor('15 октября 2010')
# print date_processor('1999 октября 1')