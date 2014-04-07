#anime-tracker.ru module
import urllib, re, os, sys, webbrowser, datetime, time
from lxml import etree
extract_data = __import__('grabber')
xpathes = {
    'name':'''(//div[@class='strTitle'])[1]//text()''',
    'name_regexp':[{'regexp':r'^\s+(.*)', 'group':r'\1'}],
    'date':'''(//td[div[@class='strTitle']])[1]//div[@class='eDetails']/text()''',
    'date_regexp':[{'regexp':r'', 'group':r''}],
    #'image':'''(//table[@class='embedded']//td[@align='center']/a[img]/img/@src)[1]''',
    #'image_regexp':[{'regexp':r'', 'group':r''}],
    'url':'''(//div[@class='strTitle'])[1]/a/@href''',
    'url_regexp':[{'regexp':r'', 'group':r''}],
}

#extraction goes here
def gather_info(url, last_out_string):
    return extract_data.grab_info(url, xpathes, last_out_string)

#for extra logic, re-define gather_info method
# def gather_info_v0(url, last_out_string):
    # #holds data to return
    # result = []
    # #setting http proxy (optional) and trying to open page
    # http_proxy=os.getenv('http_proxy')
    # if http_proxy:
        # if not http_proxy.startswith('http:'): proxy={'http':'http://'+http_proxy}
        # else: proxy={'http':http_proxy}
        # page = urllib.urlopen(str(url),proxies=proxy)
    # else:
        # page = urllib.urlopen(str(url))
    # html = page.read()
    # tree = etree.HTML(html)
    # #extracts newest (last) anime found
    # last_out = ''.join(tree.xpath(xpathes['name']))
    # last_out = re.sub(r'^\s+(.*)',r'\1',last_out)
    # #encoding name:
    # encoded_name=''
    # try:
        # result.append(last_out.encode('cp866'))
        # encoded_name = last_out.encode('cp866')
    # except:
        # result.append(str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('cp866', 'ignore'))
        # encoded_name = str(last_out.encode('raw_unicode_escape')).decode('Windows-1251').encode('cp866', 'ignore')
    # #extracting time and flag - new anime added or old
    # last_out_date = ''.join(tree.xpath(xpathes['date']))
    # #anime trackers: dd-mm-yyyy
    # #filtered output: 0dd-yyyy
    # last_out_date_canonical = re.sub(r'.*?\s(\d+?)\s.*?(\d{4}).*',r'0\1-\2',str(" "+last_out_date.replace('.', ' ').replace('-', ' ')))
    # last_out_dateflag = str("- new! (added today)" if str(datetime.date.today()) in str(last_out_date) or str(datetime.datetime.now().strftime('%d-%Y')) in last_out_date_canonical else "- old")
    # #if we haven't exactly this title's text -> series was changed -> add to flag
    # if not(encoded_name) in str(last_out_string.encode('cp866', 'ignore')):
        # last_out_dateflag+='; new series!'
    # result.append(last_out_dateflag)
    # last_out_image = ''.join(tree.xpath(xpathes.get('image', 'noimage.png')))
    # result.append(last_out_image)
    # if re.sub(r'.*?\/\/(.*?)\/.*',r'\1',url) in last_out:
        # # and contains(.,'720p')
        # result.append(''.join(tree.xpath(xpathes['url'])))
    # else:
        # #url don't have domain - gathering full url: http:// + domain + orig. url -> // to / -> http:/ to http://
        # result.append(str("http://"+re.sub(r'.*?\/\/(.*?\/).*',r'\1',url)+''.join(tree.xpath(xpathes['url']))).replace('//','/').replace('http:/','http://'))
    # return result