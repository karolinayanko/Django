# Create your views here.
import os, codecs, time
MODULE_ROOT = os.path.normpath(os.path.dirname(__file__))
from django.http import HttpResponse, HttpResponseNotFound
from mods.CheckanimeLastadded import extract_data_to_html, test
def showdata(request):
    #opening files -> reading -> clearing data
    anime_file_name = os.path.join(MODULE_ROOT, 'mods', 'anime_url.txt')
    temp_file_name = os.path.join(MODULE_ROOT, 'mods', 'temp.tmp')
    f = open(anime_file_name)
    links = []
    links = f.readlines()
    f.close()
    #contains data with previous latest extracted series
    last_out_string = ''
    with codecs.open(temp_file_name, encoding = 'cp866') as los:
        for item in los:
            last_out_string+=item
    #start extracting
    res = extract_data_to_html(links, last_out_string)
    return HttpResponse(res)
#writing this string - this string should init github sync