from django.shortcuts import render
from django.views.generic import ListView, DetailView # Import class, for show list of objects from DB
from .models import Post
from pprint import pprint


# Create your views here.
class PostList(ListView):
    model = Post # indicate the model, whose objects we will show
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pprint(context)
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
