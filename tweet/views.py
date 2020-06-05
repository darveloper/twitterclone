from django.shortcuts import render, redirect, get_object_or_404
from tweet.models import Tweet
from tweet.forms import CreateTweetForm, UpdateTweetPostForm
from twitteruser.models import Account
from django.contrib.auth.models import User


def create_tweet_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    form = CreateTweetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=request.user.email).first()
        obj.author = author
        obj.save()
        form = CreateTweetForm()

    context['form'] = form


    return render(request, 'create_tweet.html', context)

def detail_tweet_view(request, slug):
    context = {}

    tweet = get_object_or_404(Tweet, slug=slug)
    context['tweet'] = tweet

    return render(request, 'detail_tweet.html', context)


def edit_tweet_view(request, slug):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")
    
    tweet = get_object_or_404(Tweet, slug=slug)
    if request.POST:
        form = UpdateTweetPostForm(request.POST or None, request.FILES or None, instance=tweet)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            tweet = obj
    form = UpdateTweetPostForm(
            initial = {
                "body": tweet.body,
            }
        )
    context['form'] = form
    return render(request, 'edit_tweet.html', context)

