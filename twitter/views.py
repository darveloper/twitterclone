from django.shortcuts import render
from operator import attrgetter
from tweet.models import Tweet

def home_view(request):
    context = {}
    tweets = Tweet.objects.all().order_by('-date_updated')
    context['tweets'] = tweets
    return render(request, 'home.html', context)
