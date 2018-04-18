from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

class BlogListView(ListView):
    template_name = 'blog_list.html'
    model = Post
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
