#tt.animedia.tv module
import urllib, re, os, sys, webbrowser, datetime, time
from lxml import etree
extract_data = __import__('digester_ua.mods.grabber', fromlist = ['grab_info'])
#expressions for data gathering and handling
xpathes = {
    'name':'''(//tbody[@id='highlighted']//td[@align='left'])[1]//a/b/text()''',
    'name_regexp':[{'regexp':r'(.*?)\s\/.*?(\d+.*?)(:|\s|\]|$).*', 'group':r'\1 : \2'}],
    'date':'''(//tbody[@id='highlighted']//td[@align='left'])[1]/i/text()''',
    'date_regexp':[{'regexp':r'', 'group':r''},{'regexp':r'(.*)', 'group':r'\1'}],
    'image':'''(//table[@class='embedded']//td[@align='center']/a[img]/img/@src)[1]''',
    'image_regexp':[{'regexp':r'', 'group':r''}],
    'url':'''(//tbody[@id='highlighted']//td[@align='left'])[1]//a[b]/@href''',
    'url_regexp':[{'regexp':r'', 'group':r''}],
}
#extraction goes here
def gather_info(url, last_out_string):
    return extract_data.grab_info(url, xpathes, last_out_string)

#for extra logic, re-define gather_info method