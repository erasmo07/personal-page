from django.views.generic import TemplateView
from blog.models import Post


class Home(TemplateView):
    template_name = 'index.html'
    last_post = Post.objects.last()
