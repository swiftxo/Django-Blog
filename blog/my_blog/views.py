from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class Article(DetailView):
    model  = Post
    template_name = 'blog_post.html'

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = EditForm

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')