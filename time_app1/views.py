from django.shortcuts import render, HttpResponse, redirect
# from django.http import JsonResponse
from time import gmtime, strftime
# from datetime import datetime


# def index(request):
#     return HttpResponse("you are at the first page of the time app bro")

# from django.shortcuts import render
    


def first(request):
    return HttpResponse("wuddup yo")

def index(request):
    context = {
        'time' : strftime("%B %d, %Y", gmtime()),
        'date' : strftime("%I : %M %p", gmtime())
    }
    return render(request, "index.html", context)




# Create your views here.
