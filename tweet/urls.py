from django.urls import path
from tweet.views import(
    create_tweet_view,
    detail_tweet_view,
)

app_name = 'tweet'

urlpatterns = [
    path('create/', create_tweet_view, name="create"),
    path('<slug>/', detail_tweet_view, name="detail"),
]