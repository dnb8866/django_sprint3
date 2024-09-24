from django.db.models.manager import Manager
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category


def get_published(posts: Manager):
    """Return published posts."""
    return (
        posts
        .select_related('category', 'author', 'location')
        .filter(is_published=True,
                pub_date__lte=timezone.now(),
                category__is_published=True))


def index(request):
    """Main page for blog. Views all blog posts."""
    post_list = get_published(Post.objects)[:5]
    return render(request, 'blog/index.html', {
        'post_list': post_list
    })


def post(request, post_id):
    """View post details."""
    post_obj = get_object_or_404(
        get_published(Post.objects),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {
        'post': post_obj
    })


def category(request, category_slug):
    """View published posts in category, if pub date less than now."""
    category_obj = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    return render(request, 'blog/category.html', {
        'category': category_obj,
        'post_list': get_published(category_obj.posts)
    })
