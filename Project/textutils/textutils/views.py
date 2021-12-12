# i create this file - hari om
from django.http import HttpResponse


def index(req):
    return HttpResponse("hello world")


def about(req):
    return HttpResponse("this is about page")
