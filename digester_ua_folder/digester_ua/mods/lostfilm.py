#lostfilm.tv module
import urllib, re, os, sys, webbrowser, datetime, time
from lxml import etree
extract_data = __import__('grabber')
#expressions for data gathering and handling
xpathes = {
    'name':'''((//div[@class='mid']/div/h1/text())[1]|//*[*/tr/td//div[@id='TitleDiv1']]//tr/td//span[@class='micro']/span[2]/text())''',
    'name_regexp':[{'regexp':r'', 'group':r''}],
    'date':'''(//*[*/tr/td//div[@id='TitleDiv1']]//tr/td//span[@class='micro']/span)[1]/text()''',
    'date_regexp':[{'regexp':r'\.', 'group':r'-'},{'regexp':r'(.*?)\-(.*?)\-(.*?)\s.*', 'group':r'\3-\2-\1'}],
    'image':'''//div[@class='mid']/div[h1]/img/@src''',
    'image_regexp':[{'regexp':r'', 'group':r''}],
    'url':'''//*[*/tr/td//div[@id='TitleDiv1']]//tr/td//a[@class='a_details']/@href''',
    'url_regexp':[{'regexp':r'', 'group':r''}],
}
#extraction goes here
def gather_info(url, last_out_string):
    return extract_data.grab_info(url, xpathes, last_out_string)

#for extra logic, re-define gather_info method