from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.


def index(request):
    return HttpResponse("welcome")
