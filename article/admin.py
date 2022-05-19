from pyexpat import model
from this import d
from xml.etree.ElementTree import Comment
from django.contrib import admin
from jmespath import search

from .models import Article, Comment

# Register your models here.
admin.site.register(Comment)

@admin.register(Article)

class ArticleAadmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date","content"]

    list_display_links = ["title","created_date"]

    search_fields = ['title']

    list_filter = ["created_date"]

    class  Meta:
        model = Article
      