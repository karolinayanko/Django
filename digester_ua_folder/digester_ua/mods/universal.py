import urllib, re, os, sys, webbrowser, datetime, time, calendar
from lxml import etree
xpathes = {#ex.ua xpathes | lostfilm
    'name':'''//td/h1/text()|((//div[@class='mid']/div/h1/text())[1]|//*[*/tr/td//div[@id='TitleDiv1']]//tr/td//span[@class='micro']/span[2]/text())''',
    'date':'''//span[@class='modify_time']/text()|(//*[*/tr/td//div[@id='TitleDiv1']]//tr/td//span[@class='micro']/span)[1]/text()''',
    'image':'''(//table//td[h1]/img/@src)[1]|//div[@class='mid']/div[h1]/img/@src''',
    'url':'''//span/a[@onclick='return play_online();']/@href|//*[*/tr/td//div[@id='TitleDiv1']]//tr/td//a[@class='a_details']/@href''',
}

def gather_info(url, last_out_string):
    #holds data to return
    result = []
    #setting http proxy (optional) and trying to open page
    http_proxy=os.getenv('http_proxy')
    if http_proxy:
        if not http_proxy.startswith('http:'): proxy={'http':'http://'+http_proxy}
        else: proxy={'http':http_proxy}
        page = urllib.urlopen(str(url),proxies=proxy)
    else:
        page = urllib.urlopen(str(url))
    html = page.read()
    tree = etree.HTML(html)
    #extracts newest (last) anime found
    last_out = ' : '.join(tree.xpath(xpathes['name']))
    #encoding name:
    encoded_name=''
    try:
        result.append(last_out.encode('cp866'))
        encoded_name = last_out.encode('cp866')
    except:
        result.append(str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('cp866', 'ignore'))
        encoded_name = str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('cp866', 'ignore')
    #extracting time and flag - new anime added or old
    last_out_date = ''.join(tree.xpath(xpathes['date']))
    #anime trackers: dd-mm-yyyy
    #ex.ua: hh:mm, dd month yyyy
    #lostfilm dd.mm.yyyy hh:mm
    #filtered output: 0dd-yyyy
    last_out_date_canonical = re.sub(r'.*?\s(\d+?)\s.*?(\d{4}).*',r'0\1-\2',str(" "+last_out_date.replace('.', ' ').replace('-', ' ')))
    last_out_dateflag = str("- new! (added today)" if str(datetime.date.today()) in str(last_out_date) or str(datetime.datetime.now().strftime('%d-%Y')) in last_out_date_canonical else "- old")
    #yesterday flag
    if datetime.date.today().day == 1:
        if datetime.date.today().month == 1:
            yesterday = datetime.date.today().replace(day = 31, month = 12, year = datetime.date.today().year-1)
        else:
            yesterday = datetime.date.today().replace(day = calendar.mdays[datetime.date.today().month-1], month = datetime.date.today().month - 1)
    else:
        yesterday = datetime.date.today().replace(day = datetime.date.today().day - 1)
    last_out_dateflag += str(" - added yesterday" if str(yesterday) in str(last_out_date) or str(yesterday.strftime('%d-%Y')) in last_out_date_canonical else "")
    # print "="*10
    # print "y:str = ",yesterday.strftime('%d-%Y')
    # print "y:raw = ",yesterday
    # print "today = ",datetime.date.today()
    # print "today:str = ",datetime.datetime.now().strftime('%d-%Y')
    # print "last_out = ",last_out_date_canonical
    #if we haven't exactly this title's text -> series was changed -> add to flag
    if not(encoded_name+'\r\n') in str(last_out_string.encode('cp866', 'ignore')):
        last_out_dateflag+='; new series!'
    result.append(last_out_dateflag)
    last_out_image = ''.join(tree.xpath(xpathes['image']))
    if last_out_image:
        result.append(last_out_image)
    else:
        result.append('noimage.png')
    if re.sub(r'.*?\/\/(.*?)\/.*',r'\1',url) in last_out:
        # and contains(.,'720p')
        result.append(''.join(tree.xpath(xpathes['url'])))
    else:
        #url don't have domain - gathering full url: http:// + domain + orig. url -> // to / -> http:/ to http://
        result.append(str("http://"+re.sub(r'.*?\/\/(.*?\/).*',r'\1',url)+''.join(tree.xpath(xpathes['url']))).replace('//','/').replace('http:/','http://'))
    return result
    # print "="*10
    # print "y:str = ",yesterday.strftime('%d-%Y')
    # print "y:raw = ",yesterday
    # print "today = ",datetime.date.today()
    # print "today:str = ",datetime.datetime.now().strftime('%d-%Y')
    # print "last_out = ",last_out_date