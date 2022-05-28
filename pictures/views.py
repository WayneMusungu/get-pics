from django.shortcuts import render
from django.http  import HttpResponse
from .models import Galleria
import datetime as dt
# Create your views here.

def main(request):
    date = dt.date.today()
    return render(request, 'main.html',{"date": date})


