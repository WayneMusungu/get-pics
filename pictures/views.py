from django.shortcuts import render
from django.http  import HttpResponse
from .models import Galleria
import datetime as dt
# Create your views here.

def main(request):
    date = dt.date.today()
    post = Galleria.days_post
    return render(request, 'main.html',{"date": date,"post":post})

def search_results(request):
    if 'galleria' in request.GET and request.GET["galleria"]:
        category_term = request.GET.get('galleria')
        searchname= Galleria.search_by_category(category_term)
        message = f"{category_term}"

        return render(request, 'search.html',{"message":message, "galleria":searchname})

    else:
       message = "You haven't searched for any term"
       return render(request, 'search.html',{"message":message})


