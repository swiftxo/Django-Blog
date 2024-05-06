from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Post, Category
from .forms import PostForm,EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(Home,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class Article(DetailView):
    model  = Post
    template_name = 'blog_post.html'
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(Article,self).get_context_data(*args, **kwargs)
        like = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = like.total_likes()
        liked = False
        if like.likes.filter(id = self.request.user.id).exists():
            liked = True
        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(CreatePost,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = EditForm
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(EditPost,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class CreateCategory(CreateView):
    model = Category
    template_name = 'create_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(CreateCategory,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    category_menu = Category.objects.all()
    return render(request, 'categories.html', {
        'cats': cats.title().replace('-', ' '),
        'category_posts': category_posts,
        'category_menu': category_menu  
    })



def Likes(request,pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail',args = [str(pk)]))
