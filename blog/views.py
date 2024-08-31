from django.shortcuts import get_object_or_404, render
from blog.models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/post/list.html', locals())


def post_detail(request, year, month, day, post):
    data_post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request,'blog/post/detail.html', locals())