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
    tweet_list = [{"id":tweet.id, "content":tweet.content,"likes":random.randint(0,123312313) } for tweet in tweet_query]
    data= {
        "response": tweet_list

    }
    return JsonResponse(data)

def TweetCreateView(request):
    form = TweetsForm(request.POST or None)
    print(form)
    print("hi")
    if form.is_valid():
        print("hello")
        obj = form.save()
        print(obj)
        obj.save
        form = TweetsForm()
        return redirect("homepage")
    
    return render(request,  "components/form.html", context={"form":form})
