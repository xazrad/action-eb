from django.http import HttpResponse

def index(*args, **kwrags):
    return HttpResponse('Hello World')
