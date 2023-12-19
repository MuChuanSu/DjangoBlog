from datetime import datetime

from django.shortcuts import render, redirect

from mysite.models import Post

def homepage(request):
    posts = Post.objects.all()
    post_lists =list()
    now = datetime.now()
    return render(request,"index.html",locals())

def showpost(request,slug):
    post = Post.objects.get(slug=slug)
    try:
        if post != None:
            return render(request, "post.html", locals())
    except:
        return redirect("/")



