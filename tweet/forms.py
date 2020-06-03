from django import forms
from tweet.models import Tweet

class CreateTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['body']

class UpdateTweetPostForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['body']
    
    def save(self, commit=True):
        tweet = self.instance
        tweet.body = self.cleaned_data['body']

        if commit:
            tweet.save()
        return tweet