# Generated by Django 4.2.3 on 2023-08-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_content_author_pic_alter_article_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(default='This this a little description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.TextField(default='https://contenthub-static.grammarly.com/blog/wp-content/uploads/2022/08/BMD-3398-760x400.png'),
        ),
        migrations.AlterField(
            model_name='author',
            name='pic',
            field=models.TextField(default='https://cdn-icons-png.flaticon.com/512/206/206906.png'),
        ),
    ]
