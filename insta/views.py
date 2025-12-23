from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages
 
from .models import *

from .forms import UploadForm, RegisterForm, CommentForm
 
 
def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(form.cleaned_data["password"])

            user.save()

            return redirect("login")

    else:

        form = RegisterForm()

    return render(request, "register.html", {"form": form})
 
 
def login_view(request):

    if request.method == "POST":

        user = authenticate(

            request,

            username=request.POST["username"],

            password=request.POST["password"]

        )

        if user:

            login(request, user)

            return redirect("feed")

        messages.error(request, "Invalid credentials")
 
    return render(request, "login.html")
 
 
def logout_view(request):

    logout(request)

    return redirect("login")
 
 
@login_required

def feed(request):

    posts = Post.objects.all().order_by("-created_at")

    return render(request, "feed.html", {"posts": posts})
 
 
@login_required

def upload(request):

    if request.method == "POST":

        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.user = request.user

            post.save()

            return redirect("feed")

    else:

        form = UploadForm()
 
    return render(request, "upload.html", {"form": form})
 
 
@login_required

def like_post(request, post_id):

    post = Post.objects.get(id=post_id)

    like, created = Like.objects.get_or_create(post=post, user=request.user)

    if not created:

        like.delete()

    return redirect("feed")
 
 
@login_required

def comment_post(request, post_id):

    post = Post.objects.get(id=post_id)

    form = CommentForm(request.POST)

    if form.is_valid():

        comment = form.save(commit=False)

        comment.user = request.user

        comment.post = post

        comment.save()

    return redirect("feed")
 
 
@login_required

def profile(request, username):

    user_obj = User.objects.get(username=username)

    posts = Post.objects.filter(user=user_obj)
 
    is_following = Follow.objects.filter(follower=request.user, following=user_obj).exists()
 
    return render(request, "profile.html", {

        "user_obj": user_obj,

        "posts": posts,

        "is_following": is_following,

    })
 
 
@login_required

def follow_user(request, username):

    user_obj = User.objects.get(username=username)

    follow, created = Follow.objects.get_or_create(

        follower=request.user, following=user_obj

    )

    if not created:

        follow.delete()

    return redirect("profile", username=username)

 
