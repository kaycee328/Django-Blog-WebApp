from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (DetailView, ListView, CreateView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from users.models import Profile
from django.contrib.auth.models import User


# Create your views here.
@login_required
def home(request):
    post = Post.objects.all().order_by('-date_posted')  #'the minus sign is to sort in descending order'
    context = {
        'posts': post
    }
    return render(request, 'blogapp/index.html', context)

# THIS IS THE VIEW OF THE MAIN HOMEPAGE OF THE WEBAPP
class Homepage(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blogapp/index.html'
    ordering = ['-date_posted'] 
    context_object_name = 'posts'
    paginate_by = 3
    # queryset =  Post.objects.all().order_by('-date_posted') 

# THIS VIEW LEADS TO THE PROFILE OF ANY REGISETERD USER (ALSO SHOWS THEIR POSTS)
class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blogapp/user_post.html'
    # ordering = ['-date_posted'] 
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        context['user'] = user
        print(user)
        return context

# THIS VIEW LEADS TO THE ABOUT PAGE OF THE SITE
@login_required
def about(request):
    userdp = request.user.profile.image.url
    print(userdp)
    return render(request, 'blogapp/about.html', {'userdp': userdp})


# SHOWS THE LOGGED IN USER'S POSTS
@login_required
def userpost(request):
    userposts = Post.objects.filter(author=request.user).order_by('-date_posted')
    return render(request, 'blogapp/userpost.html', {'user_posts' : userposts})

class UserPost(ListView):
    model = Post
    template_name = 'blogapp/userpost.html'
    context_object_name = 'posts'

# TO VIEW OTHER USERS' PROFILE
class ViewUserProfile(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'blogapp/user-profile.html'
    context_object_name = 'profile'

# TO VIEW FULL DETAILS ABOUT ANY POST
class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blogapp/post_details.html'
    context_object_name = 'post'

# FOR THE LOGGED IN USER TO CREATE A NEW OPOST OF HIS OR HER CHOICE
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blogapp/post-create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})


# TO UPDATE THE CONTENT OF ANY OF YOUR POST(LOGGED-IN USER)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blogapp/post-update.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# TO DELETE A POST THAT WAS CREATED BY THE LOGGED-IN USER
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blogapp/post-delete.html'
    context_object_name = 'target'
    success_url = reverse_lazy('blog-home')
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


        