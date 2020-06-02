from django.shortcuts import render
from twitteruser.models import Account

def home_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'home.html', context)
