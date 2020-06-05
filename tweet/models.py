from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver


class Tweet(models.Model):
    body = models.TextField(max_length=240, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.body

def pre_save_tweet_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.body)
pre_save.connect(pre_save_tweet_receiver, sender=Tweet)

