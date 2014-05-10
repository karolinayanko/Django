import urllib, urllib2, cookielib, re, os, sys, webbrowser, datetime, time, calendar
from lxml import etree
extract_data = __import__('digester_ua.mods.grabber', fromlist = ['grab_info'])
#expressions for data gathering and handling
xpathes = {
    'name':'''(//tr[contains(@class,'tCenter')]//td[contains(@class,'t-title')]//div/a)[1]//text()''',
    'name_regexp':[{'regexp':r'', 'group':r''}],
    'date':'''((//tr[contains(@class,'tCenter')]//td[p and contains(@class,'nowrap')])[1]//p//text())[1]''',
    'date_regexp':[{'regexp':r'(.*?)\-(.*?)\-(.*)','group':r'20\3-\2-\1'}],
    #'image':'''(//table[@class='main']//tr/td[@align='center']/a[img]/img/@src)[1]''',
    #'image_regexp':[{'regexp':r'', 'group':r''}],
    'url':'''(//tr[contains(@class,'tCenter')]//td[contains(@class,'t-title')]//div/a)[1]/@href''',
    'url_regexp':[{'regexp':r'\.\/viewtopic(.*)', 'group':r'http://rutracker.org/forum/viewtopic\1'}],
}
#extraction goes here
def gather_info_orig(url, last_out_string):
    return extract_data.grab_info(url, xpathes, last_out_string)

#for extra logic, re-define gather_info method
def gather_info(url, last_out_string):
    #holds data to return
    result = []
    ###POST request###
    #http://rutracker.org/forum/tracker.php?nm={key}
    #http://login.rutracker.org/forum/login.php?redirect=/forum/tracker.php?nm={key}
    #http://login.rutracker.org/forum/login.php
    #login_password = animedigest
    #login_username = theredgreenblue
    #compiling POST data
    values = {'login_password' : 'animedigest',
              'login_username' : 'theredgreenblue',
              'login' : 'Aoia'}
    data = urllib.urlencode(values)
    #cookies handling
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #compiling data and POST url
    login = urllib2.Request('http://login.rutracker.org/forum/login.php', data)
    #login to site
    opener.open(login)
    #open our page with login cookies stored in custom opener
    page = opener.open(url)
    html = page.read()
    ##################
    tree = etree.HTML(html)
    #extracts newest (last) anime found
    last_out = ' : '.join(tree.xpath(xpathes['name']))
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
            encoded_name = last_out.encode('utf-8')
        else:
            result.append(str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('utf-8'))#.encode('utf-8')
            encoded_name = str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('utf-8')#.encode('utf-8')
    except Exception as ex:
        return ex + "in grabber.py module"
        # result.append(str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('cp866', 'ignore'))
        # encoded_name = str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('cp866', 'ignore')
    #extracting time and flag - new anime added or old
    last_out_date = ''.join(tree.xpath(xpathes['date']))
    from date_processor import date_processor
    last_out_date = date_processor(last_out_date)
    #last_out_date = '0'+last_out_date
    #applying regexps if any
    # if xpathes.get('date_regexp'):
        # for regexp in xpathes.get('date_regexp'):
            # if regexp != '':
                # last_out_date = re.sub(regexp, r'\1', last_out_date)
    if xpathes.get('date_regexp'):
        for regexp in xpathes.get('date_regexp'):
            if regexp.get('regexp') != '' and regexp.get('group'):
                last_out_date = re.sub(regexp.get('regexp'), regexp.get('group'), last_out_date)
    #last_out_dateflag = str("- new! (added today)" if str(datetime.date.today()) in str(last_out_date) else "- old")
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
    # modern way (using timedelta):
    yesterday = (datetime.datetime.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    yesterday_nomonth = (datetime.datetime.today()-datetime.timedelta(days=1)).strftime('%d-%Y')
    # last_out_dateflag += str(" - added yesterday" if str(yesterday) in str(last_out_date) or str(yesterday.strftime('%d-%Y')) in last_out_date else "")
    last_out_dateflag += str(" - added yesterday" if str(yesterday) in str(last_out_date) or str(yesterday_nomonth) in last_out_date else "")
    #if we haven't exactly this title's text -> series was changed -> add to flag
    if not(encoded_name+'\r\n') in str(last_out_string.encode('utf-8')):
        last_out_dateflag+='; new series!'
    result.append(last_out_dateflag)
    last_out_image = ''.join(tree.xpath(xpathes.get('image', 'noimage')))
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
    last_out_url = ''.join(tree.xpath(xpathes['url']))
    #applying regexps if any
    if xpathes.get('url_regexp'):
        for regexp in xpathes.get('url_regexp'):
            # if regexp != '':
                # last_out_url = re.sub(regexp, r'\1', last_out_url)
            if regexp.get('regexp') != '' and regexp.get('group'):
                last_out_url = re.sub(regexp.get('regexp'), regexp.get('group'), last_out_url)
    if re.sub(r'.*?\/\/(.*?)\/.*',r'\1',url) in last_out_url:
        # and contains(.,'720p')
        result.append(last_out_url)
    else:
        #url don't have domain - gathering full url: http:// + domain + orig. url -> // to / -> http:/ to http://
        result.append(str("http://"+re.sub(r'.*?\/\/(.*?\/).*',r'\1',url)+last_out_url).replace('//','/').replace('http:/','http://'))#.replace('/./','/'))
    return result

# print gather_info('http://rutracker.org/forum/tracker.php?nm=gurren+lagann', 'abcd')