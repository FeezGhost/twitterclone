from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
import random

# Create your views here.
def homeView(request):
    return render(request, "pages/home.html", context={},  status=200)

def  TweetList(request):
    tweet_query = Tweets.objects.all()
    tweet_list = [tweet.serialize() for tweet in tweet_query]
    data= {
        "response": tweet_list
    }
    return JsonResponse(data)

def TweetCreateView(request):
    form = TweetsForm(request.POST or None)
    print("ajax",request.is_ajax())
    print("hi")
    if form.is_valid():
        obj = form.save()
        print(obj)
        obj.save
        if request.is_ajax():
            data= {
                "response": obj.serialize()
            }
            return JsonResponse(data, status=201)
        form = TweetsForm()
        return redirect("homepage")
    
    return render(request,  "components/form.html", context={"form":form})
