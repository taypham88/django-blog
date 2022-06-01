from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class BlogListView(ListView):

    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by('-published_date')
    template_name = 'blogging/list.html'

class BlogDetailView(DetailView):

    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by('-published_date')
    template_name = 'blogging/detail.html'


