from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import *
from .forms import NewArticle

def index(request):
    return HttpResponse("HELLO WORLD! FROM BLOG-APP")

# Helper methods
def get_articles():
    articles = Article.objects.all()
    return articles

def showarticles(request):
    articles = Article.objects.all()
    return render(request, "blogapp/index.html", {"article_list": articles})

def detailarticle(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    print(f"ERROR : {article}")

    info = article.getinfo()
    title = info[0]
    author = get_object_or_404(Account, pk=info[1])
    detail = f"Title: {title} - Author : {author.name}"
    return render(request, "blogapp/detail.html", {"detail": detail})

def changealias(request, account_id, alias):
    author = get_object_or_404(Account, pk=account_id)
    # LOG
    old_alias = author.alias
    author.alias = alias
    author.save()

    return HttpResponse(f"NAME : {author.name}  ALIAS : {author.alias}  / OLD_ALIAS : {old_alias}")

# Handles adding new articles in the database
# TODO: An account dapat is ma automatic na ma kuha ID based ha naka login na account yana
def newarticle(request):
    if request.method == 'POST':
        form = NewArticle(request.POST)
        if form.is_valid():
            print("FORM IS VALID...")
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            try:
                print("USER ID ")
                print(title, content)
                author = Account.objects.get(request.user.id)
                print("================================")            
                
                print(f"TITLE : {title} - CONTENT : {content} - AUTHOR : {author}")
                nArticle = Article()
                nArticle.title = title
                nArticle.content = content
                nArticle.author = author
                nArticle.save()
            except TypeError as e:
                print(e)
            return render(request, 'blogapp/success.html')
    else:
        if request.user.is_authenticated:
            form = NewArticle()
        else:
            form = None
    
    return render(request, 'blogapp/newarticle.html', {'form': form})

