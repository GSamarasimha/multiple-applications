from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_queen(request):
    return HttpResponse('All ladies are queens')