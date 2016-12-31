from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache


def index(request):
    test = int(request.GET['test'])
    maxint = int(cache.get('maxint')) if cache.get('maxint') != None else test
    maxint = max(test, maxint)
    cache.set('maxint', maxint)

    return HttpResponse(maxint)