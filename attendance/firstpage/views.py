from django.shortcuts import render
from django.http import HttpResponse



def nothing(request):
    return render(request, 'startingpage.html'))

