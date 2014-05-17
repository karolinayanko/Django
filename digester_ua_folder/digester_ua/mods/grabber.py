# -*- coding: utf-8 -*-
import urllib, urllib2, re, os, sys, webbrowser, datetime, time, calendar
from lxml import etree
#latest def w/ encoding
def grab_info(url, xpathes, last_out_string):
    #holds data to return
    result = []
    res = {'name':'', 'dateflag':'', 'image':'', 'url':''}
    # page = urllib.urlopen(str(url))
    #improved: make sure that anti-bot will not ban Python. Never.
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    page = urllib2.urlopen(req)
    html = page.read()
    tree = etree.HTML(html)
    #extracts newest (last) anime found
    last_out = ' '.join(tree.xpath(xpathes['name']))
    last_out = re.sub(r'\s+',r' ',last_out)
    #applying regexps if any
    if xpathes.get('name_regexp'):
        for regexp in xpathes.get('name_regexp'):
            # if regexp != '':
                # last_out = re.sub(regexp, r'\1', last_out)
            if regexp.get('regexp') != '' and regexp.get('group'):
                last_out = re.sub(regexp.get('regexp'), regexp.get('group'), last_out)
    #encoding name:
    encoded_name=''
    try:
        if '\\u' in str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('utf-8'):
            result.append(last_out.encode('utf-8'))
            res['name']=last_out.encode('utf-8')
            encoded_name = last_out.encode('utf-8')
        else:
            result.append(str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('utf-8'))#.encode('utf-8')
            res['name']=str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('utf-8')
            encoded_name = str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('utf-8')#.encode('utf-8')
    except Exception as ex:
        return ex + "in grabber.py module"
        # result.append(str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('cp866', 'ignore'))
        # encoded_name = str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('cp866', 'ignore')
    #extracting time and flag - new anime added or old
    last_out_date = ''.join(tree.xpath(xpathes['date']))
    #print 'before regexp = ', last_out_date
    #applying regexps if any
    if xpathes.get('date_regexp'):
        for regexp in xpathes.get('date_regexp'):
            # if regexp != '':
                # last_out_date = re.sub(regexp, r'\1', last_out_date)
            if regexp.get('regexp') != '' and regexp.get('group'):
                last_out_date = re.sub(regexp.get('regexp'), regexp.get('group'), last_out_date)
    #print 'after regexp = ', last_out_date
    #applying new date-with-text processing method:
    from date_processor import date_processor
    last_out_date = date_processor(last_out_date)
    #print 'after processor = ', last_out_date
    #print 'today = ', str(datetime.date.today())
    last_out_dateflag = str("- new! (added today)" if str(datetime.date.today()) in str(last_out_date) or str(datetime.datetime.now().strftime('%d-%Y')) in last_out_date else "- old")
    #yesterday flag
    # old way:
    # if datetime.date.today().day == 1:
        # if datetime.date.today().month == 1:
            # yesterday = datetime.date.today().replace(day = 31, month = 12, year = datetime.date.today().year-1)
        # else:
            # yesterday = datetime.date.today().replace(day = calendar.mdays[datetime.date.today().month-1], month = datetime.date.today().month - 1)
    # else:
        # yesterday = datetime.date.today().replace(day = datetime.date.today().day - 1)
    yesterday = (datetime.datetime.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    yesterday_nomonth = (datetime.datetime.today()-datetime.timedelta(days=1)).strftime('%d-%Y')
    # last_out_dateflag += str(" - added yesterday" if str(yesterday) in str(last_out_date) or str(yesterday.strftime('%d-%Y')) in last_out_date else "")
    last_out_dateflag += str(" - added yesterday" if str(yesterday) in str(last_out_date) or str(yesterday_nomonth) in last_out_date else "")
    #if we haven't exactly this title's text -> series was changed -> add to flag
    if not(encoded_name+'\r\n') in str(last_out_string):#.encode('utf-8')
        last_out_dateflag+='; new series!'
    result.append(last_out_dateflag)
    res['dateflag']=last_out_dateflag
    last_out_image = ''.join(tree.xpath(xpathes.get('image', 'noimage')))
    # if last_out_image and not(re.sub(r'.*?\/\/(.*?)\/.*',r'\1',str(url))) in last_out_image:
        # last_out_image = re.sub(r'^\.\/',r'/',last_out_image)
        # last_out_image = 'http://'+re.sub(r'.*?\/\/(.*?)\/.*',r'\1',str(url))+last_out_image
    if not(last_out_image):
        last_out_image = 'https://www.google.com/images/srpr/logo11w.png'
    #applying regexps if any
    if xpathes.get('image_regexp'):
        for regexp in xpathes.get('image_regexp'):
            # if regexp != '':
                # last_out_image = re.sub(regexp, r'\1', last_out_image)
            if regexp.get('regexp') != '' and regexp.get('group'):
                last_out_image = re.sub(regexp.get('regexp'), regexp.get('group'), last_out_image)
    result.append(last_out_image)
    res['image']=last_out_image
    last_out_url = ''.join(tree.xpath(xpathes['url']))
    #applying regexps if any
    if xpathes.get('url_regexp'):
        for regexp in xpathes.get('url_regexp'):
            # if regexp != '':
                # last_out_url = re.sub(regexp, r'\1', last_out_url)
            if regexp.get('regexp') != '' and regexp.get('group'):
                last_out_url = re.sub(regexp.get('regexp'), regexp.get('group'), last_out_url)
    if re.sub(r'.*?\/\/(.*?)\/.*',r'\1',url) in last_out_url:#??? maybe need to remove # in last_out # from condition???
        # and contains(.,'720p')
        result.append(last_out_url)
        res['url']=last_out_url
    else:
        #url don't have domain - gathering full url: http:// + domain + orig. url -> // to / -> http:/ to http://
        result.append(str("http://"+re.sub(r'.*?\/\/(.*?\/).*',r'\1',url)+last_out_url).replace('//','/').replace('http:/','http://'))
        res['url']=str("http://"+re.sub(r'.*?\/\/(.*?\/).*',r'\1',url)+last_out_url).replace('//','/').replace('http:/','http://')
    return res
#################################################################################################################
def grab_info_v0(url, xpathes, last_out_string):
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
    # print last_out_date
    # print str(datetime.date.today())
    # print str(datetime.datetime.now().strftime('%d-%Y'))
    #anime trackers: dd-mm-yyyy
    #filtered output: 0dd-yyyy
    last_out_date_canonical = re.sub(r'.*?\s(\d+?)\s.*?(\d{4}).*',r'0\1-\2',str(" "+last_out_date.replace('.', ' ').replace('-', ' ')))
    last_out_dateflag = str("- new! (added today)" if str(datetime.date.today()) in str(last_out_date) or str(datetime.datetime.now().strftime('%d-%Y')) in last_out_date_canonical else "- old")
    #if we haven't exactly this title's text -> series was changed -> add to flag
    if not(encoded_name) in str(last_out_string.encode('cp866', 'ignore')):
        last_out_dateflag+='; new series!'
    result.append(last_out_dateflag)
    last_out_image = ''.join(tree.xpath(xpathes.get('image','noimage.png')))
    result.append(last_out_image)
    if re.sub(r'.*?\/\/(.*?)\/.*',r'\1',url) in last_out:
        # and contains(.,'720p')
        result.append(''.join(tree.xpath(xpathes['url'])))
    else:
        #url don't have domain - gathering full url: http:// + domain + orig. url -> // to / -> http:/ to http://
        result.append(str("http://"+re.sub(r'.*?\/\/(.*?\/).*',r'\1',url)+''.join(tree.xpath(xpathes['url']))).replace('//','/').replace('http:/','http://'))
    return result