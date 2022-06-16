from django.contrib.auth.decorators import login_required

from msilib.schema import ListView
from pdb import post_mortem
from django.shortcuts import render
from django.http import HttpResponse
from .models import User_posts
from .forms import User_postsForm


# Create your views here.
def index (request):
    full_post = User_posts.objects.all()
    obj = User_posts.objects.filter()
    context = {"object": obj, "full_post": full_post}
    return render(request, "posts/index.html", context)

def home_view(request, my_id):
    obj = User_posts.objects.get(id=my_id)
    context = {"object": obj}
    return render(request, "posts/home.html", context)

@login_required
def user_posts_create(request):
    form = User_postsForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = User_postsForm()
    context = {
        'form': form
    }
    return render(request, "posts/post_create.html", context)
