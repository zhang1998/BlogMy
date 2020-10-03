from django.shortcuts import render,get_object_or_404
from .models import article
from django.http import HttpResponse
# Create your views here.

# get title

def blog_title(request):
    blogs=article.objects.all()
    return render(request,"blog/titles.html",{"sblogs":blogs})
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def blog_article(request,article_id):
    art=get_object_or_404(article,id=article_id)
    pub=article.publish
    return render(request,"blog/content.html",{"article":art,"publish":pub})
