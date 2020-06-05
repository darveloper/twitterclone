from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from operator import attrgetter
from tweet.models import Tweet

@login_required
def home_view(request):
    context = {}
    tweets = Tweet.objects.all().order_by('-date_updated')
    context['tweets'] = tweets
    return render(request, 'home.html', context)
