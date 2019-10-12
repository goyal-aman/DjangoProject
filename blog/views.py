from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    CreateView,
     DetailView,
     ListView,
     UpdateView,
     DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post


# def home(request):

#     context = {"posts": Post.objects.all()}


#     return render(request, "blog/home.html", context)


class PostListView(ListView):
    '''home page'''
    model = Post
    template_name = "blog/home.html"  # <app>/<models>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UserPostListView(ListView):
    '''home page'''
    model = Post
    template_name = "blog/user_post.html"  # <app>/<models>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"] #will be overridden
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    """
    default location where this class will
    search the template is
    #<app>/<models>_<viewtype>.html
    """


def about(reques):
    return render(reques, "blog/about.html", {"title": "wow"})


"""
to remembr
from django.http import HttpResponse
return HttpResponse('<h1>blog about</h1>')
"""
