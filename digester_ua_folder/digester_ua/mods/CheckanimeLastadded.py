#!/usr/bin/python
# -*- coding: utf-8 -*-
#importing libs: opening sites, regexps, std libs, webbrowser to open url in brwsr, time libs, smtp mail lib, multithreading, opening files with diff encodings
import urllib, re, os, sys, webbrowser, datetime, time, smtplib, threading, codecs
from sender import sendmail
from multi_threading import Thread
reload(sys)
#cp1251
sys.setdefaultencoding('utf-8')
from lxml import etree
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Header import make_header
from email.Utils import formatdate
#server params
server = 'smtp.gmail.com'
port = 587
#mail encoding
icharset = 'cp866'
# def extract_data(links, last_out_string):
    # count = 0
    # new_series_added=False
    # series_string=''
    # last_out_link = []
    # for url in links:
        # url = url.replace('\n','')
        # result = []
        # #calling gather_info
        # try:
            # if 'anidub' in url:
                # module = __import__('anidub')
                # result = module.gather_info(url, last_out_string)
            # elif 'rutracker' in url:
                # module = __import__('rutracker_org')
                # result = module.gather_info(url, last_out_string)
            # elif 'animedia' in url:
                # module = __import__('animedia')
                # result = module.gather_info(url, last_out_string)
            # elif 'ex.ua' in url:
                # module = __import__('ex_ua')
                # result = module.gather_info(url, last_out_string)
            # elif 'lostfilm' in url:
                # module = __import__('lostfilm')
                # result = module.gather_info(url, last_out_string)
            # elif 'anime-tracker.ru' in url:
                # module = __import__('animetracker_ru')
                # result = module.gather_info(url, last_out_string)
            # elif 'filmix.net' in url:
                # module = __import__('filmix_net')
                # result = module.gather_info(url, last_out_string)
            # # else:
                # # module = __import__('universal')
                # # result = module.gather_info(url, last_out_string)
        # except Exception as ex:
            # print ex
            # print "Error loading url: "+url
            # continue
        # domain = str(count+1)+". "+re.sub(r'.*?\/\/(.*?)\/.*',r'\1',str(url))
        # #temporary dummy for filtering name - do not filter except 2 domains:
        # #if 'anidub' in url or 'animedia' in url:
        # # if 'animedia' in url:
            # # #anime_info = re.sub(r'(.*?)\s\/.*?(\d+.*?)(:|\s|\]).*',r'\1 : \2',str(result[0]+":"))
            # # #cutting, if ":" in the end of text ex. Title x name : -> Title x name
            # # anime_info = re.sub(r'(.*?)\s\/.*?(\d+.*?)(:|\s|\]).*',r'\1 : \2',str(result[0]+":").replace(' - ','-').replace('- ','-').replace(' -','-'))
            # # anime_info = re.sub(r'(.*):$',r'\1',anime_info)
        # # else:
        # anime_info = re.sub(r'\s+',r' ',str(result[0]).replace(' - ','-').replace('- ','-').replace(' -','-'))
        # #collecting new extracted names data
        # series_string+=result[0]+'\n'
        # #move flag to True, if at least 1 anime has a new series
        # if 'new series' in str(result[1]):
            # new_series_added=True
        # is_new_flag = str(result[1])
        # last_out_link.append(result[3])
        # print domain, is_new_flag
        # print anime_info
        # count += 1
    # #write to file if we have changes in new series
    # if new_series_added:
        # with open('temp.tmp', 'w') as file:
            # file.write(series_string)
    # return open_page(last_out_link)
# def open_page(links):
    # print "=================================================="
    # page = raw_input("Open site? (n - continue, Number - page number):")
    # if page != 'n' and int(page) > 0 and int(page) <= len(links):
        # webbrowser.open(links[int(page)-1])
    # refresh = raw_input("Refresh data? (y - yes, else - stop):")
    # if refresh.lower()[0] == 'y':
        # return True
    # else: return False

# @Thread
# def digest_sender():
    # count = 0
    # new_series_added=False
    # series_string=''
    # # try:
    # #check: if time is 8, 12, 18 hrs -> start parsing
    # if ('8' in str(datetime.datetime.now().hour) or '12' in str(datetime.datetime.now().hour) or '18' in str(datetime.datetime.now().hour)):
        # #open files
        # last_out_string = ''
        # with codecs.open('temp.tmp', encoding = 'cp866') as los:
            # for item in los:
                # last_out_string+=item
        # m = open('mails.txt')
        # mails = m.readlines()
        # m.close()
        # f = open('anime_url.txt')
        # links = []
        # links = f.readlines()
        # f.close()
        # #composing message
        # digest_message = '<html><body><h3>Daily Anime Digest '+str(datetime.date.today())+'</h3><hr><table cellpadding="4" cellspacing="2" border="0">'
        # for url in links:
            # url = url.replace('\n','')
            # result = []
            # #calling gather_info
            # try:
                # if 'anidub' in url:
                    # module = __import__('anidub')
                    # result = module.gather_info(url, last_out_string)
                # elif 'rutracker' in url:
                    # module = __import__('rutracker_org')
                    # result = module.gather_info(url, last_out_string)
                # elif 'animedia' in url:
                    # module = __import__('animedia')
                    # result = module.gather_info(url, last_out_string)
                # elif 'ex.ua' in url:
                    # module = __import__('ex_ua')
                    # result = module.gather_info(url, last_out_string)
                # elif 'lostfilm' in url:
                    # module = __import__('lostfilm')
                    # result = module.gather_info(url, last_out_string)
                # elif 'anime-tracker.ru' in url:
                    # module = __import__('animetracker_ru')
                    # result = module.gather_info(url, last_out_string)
                # # else:
                    # # module = __import__('universal')
                    # # result = module.gather_info(url, last_out_string)
            # except:
                # continue
            # #collecting fresh extracted names
            # series_string+=result[0]+'\n'
            # #move flag to True, if at least 1 anime has a new series
            # if 'new series' in str(result[1]):
                # new_series_added=True
            # is_new_flag = str(result[1])
            # #adding anime to digest if it is new, creating message block:
            # if 'new! (added today)' in is_new_flag or 'new series' in is_new_flag:
                # domain = re.sub(r'.*?\/\/(.*?)\/.*',r'\1',str(url))
                # #temporary dummy for filtering name - do not filter except 2 domains:
                # #old: anime_info = re.sub(r'(.*?)\s\/.*?(\d+.*?)(:|\s|\]).*',r'\1 : \2',str(result[0]+":"))
                # # if 'anidub' in url or 'animedia' in url:
                # # if 'animedia' in url:
                    # # anime_info = re.sub(r'(.*?)\s\/.*?(\d+.*?)(:|\s|\]).*',r'\1 : \2',str(result[0]+":").replace(' - ','-').replace('- ','-').replace(' -','-'))
                    # # #cutting, if ":" in the end of text ex. Title x name : -> Title x name
                    # # anime_info = re.sub(r'(.*):$',r'\1',anime_info)
                # # else:
                # anime_info = re.sub(r'\s+',r' ',str(result[0]).replace(' - ','-').replace('- ','-').replace(' -','-'))
                # image_url = str(result[2])
                # #if img_url is cutted - "/something/etc.jpg", we'll gather this url: http://+domain+url
                # if image_url.startswith('/'):
                    # image_url = str('http://'+domain+image_url)
                # #else we'll try(!) to replace in "./something/etc.jpg" the "./" part to http://+domain+/
                # else:
                    # image_url = image_url.replace('./',str('http://'+domain+'/'))
                # digest_message += str('<tr><td><img src="'+image_url+'" align="left" height="95" width="75"></img></td><td>'+domain+' '+is_new_flag+'<br><b>'+anime_info+'</b><br><a href="'+result[3]+'" target="_blank">Download</a></td></tr>')
            # count += 1
        # digest_message += '</table></body></html>'
        # #check: if 1 or more new anime added -> send digest
        # if ('<tr><td>' in digest_message):
            # mails_clr = []
            # for m in mails:
                # mails_clr.append(m.replace('\n',''))
            # for mail in mails_clr:
                # sendmail(str(mail), 'Anime daily digest', str(digest_message))
            # #don't forget to write in file that new series added!
            # if new_series_added:
                # with open('temp.tmp', 'w') as file:
                    # file.write(series_string)
            # #and then make sleep 55 mins to make sure digest won't be sent again this hour
            # time.sleep(3300)
    # time.sleep(300)
    # #recursion
    # return digest_sender()
    # # except:
        # # return digest_sender()
# #starting hourly digest sender in parallel thread
# digest_sender()
# flag = True
# #starting user menu - update-on-demand
# while flag:
    # #print "=================================================="
    # try:
        # #opening files -> reading -> clearing data
        # f = open('anime_url.txt')
        # links = []
        # links = f.readlines()
        # f.close()
        # #contains data with previous latest extracted series
        # last_out_string = ''
        # with codecs.open('temp.tmp', encoding = 'cp866') as los:
            # for item in los:
                # last_out_string+=item
        # #start extracting
        # flag = extract_data(links, last_out_string)
        # print "=================================================="
    # except:
        # continue


##################################################################################################
MODULE_ROOT = os.path.normpath(os.path.dirname(__file__))
def extract_data_to_html(links, last_out_string):
    count = 0
    new_series_added=False
    series_string = ''
    result_string='<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body><h3>Daily Anime Digest '+str(datetime.date.today())+'</h3><hr><table cellpadding="4" cellspacing="2" border="0">'
    last_out_link = []
    for url in links:
        url = url.replace('\n','')
        #result = []
        result = {}
        #calling gather_info
        try:
            if 'anidub' in url:
                module = __import__('digester_ua.mods.anidub', fromlist = ['gather_info'])
                result = module.gather_info(url, last_out_string)
            elif 'rutracker' in url:
                module = __import__('digester_ua.mods.rutracker_org', fromlist = ['gather_info'])
                result = module.gather_info(url, last_out_string)
            elif 'animedia' in url:
                module = __import__('digester_ua.mods.animedia', fromlist = ['gather_info'])
                result = module.gather_info(url, last_out_string)
            elif 'ex.ua' in url:
                module = __import__('digester_ua.mods.ex_ua', fromlist = ['gather_info'])
                result = module.gather_info(url, last_out_string)
            elif 'lostfilm' in url:
                module = __import__('digester_ua.mods.lostfilm', fromlist = ['gather_info'])
                result = module.gather_info(url, last_out_string)
            elif 'anime-tracker.ru' in url:
                module = __import__('digester_ua.mods.animetracker_ru', fromlist = ['gather_info'])
                result = module.gather_info(url, last_out_string)
            elif 'filmix.net' in url:
                module = __import__('digester_ua.mods.filmix_net', fromlist = ['gather_info'])
                result = module.gather_info(url, last_out_string)
            # else:
                # module = __import__('universal')
                # result = module.gather_info(url, last_out_string)
        except Exception as ex:
            #print ex
            #print "Error loading url: "+url
            return ex
            continue
        domain = str(count+1)+". "+re.sub(r'.*?\/\/(.*?)\/.*',r'\1',str(url))
        #temporary dummy for filtering name - do not filter except 2 domains:
        #if 'anidub' in url or 'animedia' in url:
        # if 'animedia' in url:
            # #anime_info = re.sub(r'(.*?)\s\/.*?(\d+.*?)(:|\s|\]).*',r'\1 : \2',str(result[0]+":"))
            # #cutting, if ":" in the end of text ex. Title x name : -> Title x name
            # anime_info = re.sub(r'(.*?)\s\/.*?(\d+.*?)(:|\s|\]).*',r'\1 : \2',str(result[0]+":").replace(' - ','-').replace('- ','-').replace(' -','-'))
            # anime_info = re.sub(r'(.*):$',r'\1',anime_info)
        # else:
        #anime_info = re.sub(r'\s+',r' ',str(result[0]).replace(' - ','-').replace('- ','-').replace(' -','-'))
        anime_info = re.sub(r'\s+',r' ',str(result.get('name')).replace(' - ','-').replace('- ','-').replace(' -','-'))
        #collecting new extracted names data
        #series_string+=result[0]+'\n'
        series_string+=result.get('name')+'\n'
        ###########image url check and update#################
        #image_url = str(result[2])
        image_url = str(result.get('image'))
        #if img_url is cutted - "/something/etc.jpg", we'll gather this url: http://+domain+url
        if image_url.startswith('/'):
            image_url = str('http://'+re.sub(r'.*?\/\/(.*?)\/.*',r'\1',str(url))+image_url)
        #else we'll try(!) to replace in "./something/etc.jpg" the "./" part to http://+domain+/
        else:
            image_url = image_url.replace('./',str('http://'+re.sub(r'.*?\/\/(.*?)\/.*',r'\1',str(url))+'/'))
        # result_string+=result[0]+' '+result[1]+'<br>'+result[2]+'<br>'+result[3]+'<br><br>'
        #move flag to True, if at least 1 anime has a new series
        #
        if 'new series' in str(result.get('dateflag')):
            new_series_added=True
        #is_new_flag = str(result[1])
        is_new_flag = str(result.get('dateflag'))
        #last_out_link.append(result[3])
        last_out_link.append(result.get('url'))
        #result_string+=str('<tr><td><img src="'+image_url+'" align="left" height="95" width="75"></img></td><td>'+domain+' '+is_new_flag+'<br><b>'+anime_info+'</b><br><a href="'+result[3]+'" target="_blank">Download</a></td></tr>')
        result_string+=str('<tr><td><img src="'+image_url+'" align="left" height="95" width="75"></img></td><td>'+domain+' '+is_new_flag+'<br><b>'+anime_info+'</b><br><a href="'+result.get('url')+'" target="_blank">Download</a></td></tr>')
        count += 1
    result_string += '</table></html></body>'
    #write to file if we have changes in new series
    if new_series_added:
        with open(os.path.join(MODULE_ROOT, 'temp.tmp'), 'w') as file:
            file.write(series_string)
    return result_string
    
def test(links, last_out_string):
    return last_out_string
##################################################################################################