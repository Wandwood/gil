from audioop import reverse
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from pdb import post_mortem
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import User, User_posts
from .forms import User_postsForm
from django.db.models import Q

# Create your views here.
def index (request):
    obj = User_posts.objects.filter()
    posts_list = User_posts.objects.all().order_by('-post_date')
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"object": obj,"page_obj": page_obj}
    return render(request, "posts/index.html", context)

def detail_view(request, my_id):
    obj = User_posts.objects.get(id=my_id)
    context = {"object": obj}
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    else:
        return render(request, "posts/detail.html", context)

@login_required
def user_posts_create(request):
    form = User_postsForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/')
    form = User_postsForm()
    context = {
        'form': form
    }
    return render(request, "posts/post_create.html", context)

def user_posts_detail_view(request):
    logged_in_user_posts = User_posts.objects.filter(user=request.user)
    context = {"object": logged_in_user_posts}
    return render (request, "posts/user_posts.html", context)

def user_search_view(request):
    if request.method == "POST":
        q = request.POST['q']
        obj = User_posts.objects.filter(Q(game_name__contains=q)| Q(post_header__contains=q))
        context = {"object": obj, "q": q}
    return render(request, "posts/search.html", context)