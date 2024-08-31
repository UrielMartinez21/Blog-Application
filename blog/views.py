from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    """
    This view will display a list of posts with pagination.
    """
    post_list = Post.published.all()

    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,'blog/post/list.html', locals())


def post_detail(request, year, month, day, post):
    """
    This view will display a single post.
    """

    data_post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request,'blog/post/detail.html', locals())