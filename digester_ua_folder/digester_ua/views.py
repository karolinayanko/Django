# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
def home(request):
    res = '<h1>Page was found</h1>'
    res += '<h2>This is my first page</h2>'
    return HttpResponse(res)

def test(request):
    res = '<h1>Page was found</h1>'
    res += '<h2>This is my test page - second view in views.py</h2>'
    return HttpResponse(res)