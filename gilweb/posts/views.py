from django.shortcuts import render
from django.http import HttpResponse
from .models import User_posts
# Create your views here.
def index (request):
    return HttpResponse("я в ахуе, если честно")

def home_view(request, *args, **kwargs):
    obj = User_posts.objects.get(id=2)
    context = {"object": obj}
    return render(request, "posts/home.html", context)