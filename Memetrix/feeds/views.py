from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(redirect_field_name="login_required", login_url="/login/")
def feeds(request):
    return render(request, "feeds.html", context={"title": "MemeTrix | Feeds"})
