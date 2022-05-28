from django.shortcuts import render
from django.http  import HttpResponse
from .models import Galleria
import datetime as dt
# Create your views here.

def main(request):
    date = dt.date.today()
    post = Galleria.days_post
    return render(request, 'main.html',{"date": date,"post":post})


