from django.db import models

class Article(models.Model):
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    author_image = models.TextField(default='https://cdn-icons-png.flaticon.com/512/206/206906.png')
    author_bio = models.TextField(default="Author bio")
    title = models.CharField(max_length=200)
    description = models.TextField(default="This this a little description")
    publication_date = models.DateTimeField()
    reading_time_minutes = models.PositiveIntegerField()
    article_image = models.TextField(default='https://contenthub-static.grammarly.com/blog/wp-content/uploads/2022/08/BMD-3398-760x400.png')
    views = models.PositiveIntegerField(default=0)  # Number of views for popularity
    content = models.TextField(default="Article content")
 

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save()

    class Meta:
        ordering = ['-views']  # Tri par ordre décroissant des vues
