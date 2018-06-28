from django.conf.urls import url, include
from django.views.generic import DetailView, ListView
from blog.models import BlogPost

urlpatterns = [
    url('$', ListView.as_view(queryset=BlogPost.objects.all().order_by("-date")[:25], template_name="blog/blog.html")),
    url('(?P<pk>\d+)$', DetailView.as_view(model=BlogPost, template_name='blog/blogPost.html')),
]