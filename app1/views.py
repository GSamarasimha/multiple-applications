from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_king(request):
    return HttpResponse('king rule the kingdom')