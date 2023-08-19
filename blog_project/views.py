from django.shortcuts import render
from articles.models import Article
import random

def home(request):
    article_id = random.choice(Article.objects.values_list('id', flat=True))
    sport = Article.objects.filter(category = 'Sport').order_by('-publication_date').first()
    tech = Article.objects.filter(category = 'Tech').order_by('-publication_date').first()
    politics = Article.objects.filter(category = 'Politics').order_by('-publication_date').first()
    main_article = Article.objects.get(pk = article_id)
    secondary_articles = Article.objects.filter(category = main_article.category).exclude(pk = article_id).order_by('-publication_date')[:4]
    most_viewed_articles = Article.objects.all()[:3]
    output = {
        'sport': sport ,
        'tech': tech,
        'politics': politics,
        'main_article': {'info':main_article, 'content': main_article.content.split('\n')},
        'secondary_articles': {'1': secondary_articles[0] , '2': secondary_articles[1] , '3': secondary_articles[2] , '4': secondary_articles[3]},
        'most_view_articles' : {'1': most_viewed_articles[0], '2': most_viewed_articles[1], '3': most_viewed_articles[2]}
            } 

    return render(request,'index.html', output)
