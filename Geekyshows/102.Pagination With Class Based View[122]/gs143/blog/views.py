from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    ordering=['id']
    paginate_by=3
    paginate_orphans=1

    def get_context_data(self,*args,**kwargs):
        try:
            return super(PostListView,self).get_context_data(*args,**kwargs)
        except Http404:
            self.kwargs['page']=1
            return super(PostListView,self).get_context_data(*args,**kwargs)

class PostDetailView(DetailView):
    model=Post
    template_name='blog/post.html'