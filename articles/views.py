from django.shortcuts import render
from .models import  Article


def sport(request, category, article_id):
    sport = Article.objects.filter(category = 'Sport').order_by('-publication_date').first()
    tech = Article.objects.filter(category = 'Tech').order_by('-publication_date').first()
    politics = Article.objects.filter(category = 'Politics').order_by('-publication_date').first()
    main_article = Article.objects.get(pk = article_id)
    main_article.increase_views()
    secondary_articles = Article.objects.filter(category = category).exclude(pk = article_id).order_by('-publication_date')[:4]
    output = {
        'sport': sport ,
        'tech': tech,
        'politics': politics,
        'main_article': {'info':main_article, 'content': main_article.content.split('\n')},
        'secondary_articles': {'1': secondary_articles[0] , '2': secondary_articles[1] , '3': secondary_articles[2] , '4': secondary_articles[3]} 
            }
    return render(request,'sport.html', output)
