from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Post


def display_post(request, post_slug):

    post = Post.objects.get(slug=post_slug)

    template_data = {'post': post}
    template = "blog/post.html"

    return render_to_response(
        template,
        template_data,
        context_instance=RequestContext(request)
    )


def list_posts(request):
    template_data = {'posts': Post.objects.all()}
    template = "blog/index.html"
    return render_to_response(
        template,
        template_data,
        context_instance=RequestContext(request)
    )
