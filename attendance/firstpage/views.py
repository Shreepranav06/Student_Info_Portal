from django.shortcuts import render
from django.http import HttpResponse



def nothing(request):
    return HttpResponse("STARTING PAGE")

