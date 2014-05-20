DEVLOG
12.03.13: added new series detection;
19.03.13: added full last_out (name) encoding, removing bad : in the end of the name; "new series detection" works stable
21.03.13: fixed "new series detection" - worked badly with new encoding; updated
@todo1: debugging, flexibility, ADD! ' '.join to all tree.xpath in gather_info
!test and debug "new series detection" function!
!!tested. Exrraction is correct. ADD history to digest - append previous extraction to current mail.
21.10.13: upd. to v1.1 - added anidub and universal modules; beta-testing of module separation
21.10.13: added - dict.get(key, default=None) to image xpath !test only, will be applied on all, now only in animetracker_ru
21.10.13: added animetracker_ru.py module
22.10.13: added grabber.py - generic extraction module; changed anidub.py to work with grabber.py
22.10.13: updated new series detection - if not(encoded_name+'\r\n'), added name regexp to anidub
27.10.13: added rutracker module - in BETA testing
@todo2: implement "added yesterday" flag; debug all modules
29.10.13: implemented "added yesterday" flag in grabber.py
29.10.13: upd. grabber.py to use modern regex filters in site_modules; updated "added yesterday" in grabber.py
29.10.13: added animedia module; updated main file to use ready anime_info for anidub and animedia (w\o regexps)
29.10.13: removed anidub and animedia regexps from universal.py
@todo3: implement separate sitedefs to all sites; add http://filmix.net/ support
30.10.13: moved animetracker_ru.py to use grabber module; removed join names with :
30.10.13: implemented "added yesterday" flag in rutracker.py; added filmix_net.py module;
30.10.13: filmix_net.py - problems with encoding; do not use it for now
01.11.13: fixed "added yesterday" flag when day = 1 or date is 01.01.20xx; fixed date in rutracker (1-2013 -> 01-2013)
01.11.13: added ex_ua.py and lostfilm.py; universal.py is not needed @todo3 - DONE.
01.11.13: updated "added yesterday" flag with timedelta in grabber.py and rutracker.py; in-test
01.11.13: grabber.py and rutracker.py - need to remove import calendar (not needed); v1.2 started
03.11.13: fixed date extraction in lostfilm - regex added
07.11.13: added date_processor.py to modify date-with-text-month to normal view !in beta-test; updated regexps in ex_ua and rutracker
07.11.13: added date_processor import to grabber.py and rutracker.py
08.11.13: improved date_processor - if we have a day "1" and not "01" - adding zero to it (2013-11-8 -> 2013-11-08); updated some regexes due to it; removed adding zero to last_out_date in rutracker
@todo4: make one call in result = module.gather_info(url, last_out_string), not in each if-else condition; add import "reload" to be able to update modules in-real-time
12.05.14: added Magic Brovser to aviod antibot
15.05.14: updated to dict with crawled data in grabber.py and CheckanimeLastadded.py, rutracker_org.py

files:
anime_url - contains urls to crawl;
mails - list of url to send Anime Digest;
temp.tmp - temporary file to save last series added (!do not touch!);
xpathes - contains xpath expressions that applies on pages to crawl.

xpathes file structure (not needed now):
1. name xpath;
2. date xpath;
3. image xpath;
4. url to last series xpath.
NOTE! only english is allowed in xpathes

Supports:
-tr.anidub.com
-tt.animedia.tv
-ex.ua
-lostfilm.tv
-rutracker.org
-anime-tracker.ru
-filmix.net (not using - problems with encoding. will be used after Django implementing)
Theoretically, should work in others open-info sites

Programmers memo:
gather_info returns a list: ['name', 'is_new_flag', 'img_url', 'link to download']
NEW! returns a dict: res = {'name':'', 'dateflag':'', 'image':'', 'url':''}

sitedef xpathes structure:
xpathes = {
    'name':'''name_xpath''',
    'name_regexp':[{'regexp':r'name_regexp', 'group':r'name_regexp_group'}],
    'date':'''date_xpath''',
    'date_regexp':[{'regexp':r'date_regexp', 'group':r'date_regexp_group'},{'regexp':r'(.*)', 'group':r'\1'}],
    'image':'''image_xpath''',
    'image_regexp':[{'regexp':r'image_regexp', 'group':r'image_regexp_group'}],
    'url':'''urltoprod_xpath''',
    'url_regexp':[{'regexp':r'urltoprod_regexp', 'group':r'urltoprod_regexp_group'}],
}

NOTICE! date should be extraxted in format: Y-m-d OR d-Y in all projects (with help of regexps)

http://www.py2exe.org/index.cgi/Tutorial