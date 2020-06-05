from django.urls import path
from django.conf.urls import url 
from tweet.views import(
    create_tweet_view,
    detail_tweet_view,
    edit_tweet_view,

)


app_name = 'tweet'

urlpatterns = [
    path('create/', create_tweet_view, name="create"),

    path('<slug>/', detail_tweet_view, name="detail"),
    path('<slug>/edit', edit_tweet_view, name="edit"),
]