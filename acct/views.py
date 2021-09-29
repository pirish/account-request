from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Request an account")

def create_request(request, account_type):
    return HttpResponse("You're requesting account type %s." % account_type)
