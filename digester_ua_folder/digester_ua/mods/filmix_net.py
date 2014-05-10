#filmix.net module
import urllib, re, os, sys, webbrowser, datetime, time
from lxml import etree
extract_data = __import__('digester_ua.mods.grabber', fromlist = ['grab_info'])
#expressions for data gathering and handling
xpathes = {
    'name':'''(//div[@id='dle-content']//div[@class='block']//h2)[1]//a//text()''',
    'name_regexp':[{'regexp':r'', 'group':r''}],
    'date':'''(//div[@id='dle-content']//div[@class='body']//div[@class='info-box-2'])[1]//li[@class='added']//text()''',
    'date_regexp':[{'regexp':r'', 'group':r''}],
    'image':'''((//div[@id='dle-content']//div[@class='block']//div[@class='body']//div[contains(@id,'news-id')])[1]/a//img/@src)[1]''',
    'image_regexp':[{'regexp':r'', 'group':r''}],
    'url':'''(//div[@id='dle-content']//div[@class='block']//h2)[1]//a/@href''',
    'url_regexp':[{'regexp':r'', 'group':r''}],
}
#extraction goes here
def gather_info(url, last_out_string):
    return extract_data.grab_info(url, xpathes, last_out_string)

#for extra logic, re-define gather_info method
###result.append(unicode(str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('cp866', 'ignore'), 'unicode-escape'))
#a = gather_info('http://filmix.net/?do=search&subaction=search&story=one%20piece','asd')
#test = re.sub(r'\\u20\d\d',r'',a[0].decode('cp866'))
#print unicode(test.encode('raw_unicode_escape'), 'unicode-escape')
###
#import unicodedata
#print unicode(unicodedata.normalize('NFKD', test).encode('ascii','ignore'), 'unicode-escape')