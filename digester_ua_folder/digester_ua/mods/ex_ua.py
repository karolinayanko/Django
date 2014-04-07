#ex.ua module
import urllib, re, os, sys, webbrowser, datetime, time
from lxml import etree
extract_data = __import__('grabber')
#expressions for data gathering and handling
xpathes = {
    'name':'''//td/h1/text()''',
    'name_regexp':[{'regexp':r'', 'group':r''}],
    'date':'''//span[@class='modify_time']/text()''',
    'date_regexp':[{'regexp':r'.*,\s+(.*)', 'group':r'\1'},{'regexp':r'(.*?)\s(.*?)\s(.*)', 'group':r'\3 \2 \1'},{'regexp':r'(.*?)\s0(\d{2})$', 'group':r'\1 \2'},{'regexp':r'(.*)', 'group':r'\1'}],#,{'regexp':r'.*?\s(\d+?)\s.*?(\d{4}).*', 'group':r'0\1-\2'}
    'image':'''(//table//td[h1]/img/@src)[1]''',
    'image_regexp':[{'regexp':r'', 'group':r''}],
    'url':'''//span/a[@onclick='return play_online();']/@href''',
    'url_regexp':[{'regexp':r'', 'group':r''}],
}
#extraction goes here
def gather_info(url, last_out_string):
    return extract_data.grab_info(url, xpathes, last_out_string)

#for extra logic, re-define gather_info method