# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
def test_two(request):
    res = '<h1>Page was found</h1>'
    res += '<h2>This is my test page - second view outside views.py</h2>'
    return HttpResponse(res)