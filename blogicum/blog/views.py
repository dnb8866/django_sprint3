from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category


def index(request):
    """Main page for blog. Views all blog posts."""
    context = {
        'post_list': (
            Post.objects
            .select_related('location', 'author')
            .filter(Q(is_published=True)
                    & Q(category__is_published=True)
                    & Q(pub_date__lte=timezone.now()))[:5]
        )
    }
    return render(request, 'blog/index.html', context)


def post(request, post_id):
    """View post details."""
    context = {
        'post': get_object_or_404(
            Post.objects.filter(
                pub_date__lte=timezone.now(),
                is_published=True,
                category__is_published=True
            ),
            pk=post_id
        )
    }
    return render(request, 'blog/detail.html', context)


def category(request, category_slug):
    """View published posts in category, if pub date less than now."""
    context = {
        'category': get_object_or_404(
            Category.objects.filter(is_published=True),
            slug=category_slug
        ),
        'post_list': (
            Post.objects
            .select_related('location', 'author')
            .filter(Q(category__slug=category_slug)
                    & Q(is_published=True)
                    & Q(pub_date__lte=timezone.now()))
        )
    }
    return render(request, 'blog/category.html', context)
