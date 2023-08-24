from django.shortcuts import render
from django.views.generic import ListView, DetailView # Import class, for show list of objects from DB
from .models import Post
from datetime import datetime

# Create your views here.
class PostList(ListView):
    model = Post # indicate the model, whose objects we will show
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
