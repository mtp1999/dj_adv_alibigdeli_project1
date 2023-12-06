from django import template
from appBlog.models import Category, Post, Comment

register = template.Library()


@register.inclusion_tag("appBlog/_blog-category-section.html")
def category_section():
    cat_dict = {}
    for category in Category.objects.all():
        cat_dict[category.name] = category.post_set.filter(status=1).count()
    return {"categories": cat_dict.items()}


@register.inclusion_tag("appBlog/_blog-author-section.html")
def author_section():
    posts = Post.objects.all()
    authors = set([post.author for post in posts])
    return {"authors": authors}


@register.inclusion_tag("appBlog/_blog-latest-posts-section.html")
def latest_posts(number=3):
    posts = Post.objects.filter(status=1).order_by("-published_date")[:number]
    return {"posts": posts}


@register.inclusion_tag("appBlog/_blog-last-3-posts.html")
def last_3_posts():
    posts = Post.objects.filter(status=1).order_by("-published_date")[:3]
    return {"posts": posts}


@register.simple_tag
def counting_post_comments(post_id):
    return Comment.objects.filter(post=post_id, allowed=True).count()


@register.inclusion_tag("appBlog/_blog-tag-section.html")
def tag_section():
    tags = []
    for post in Post.objects.all():
        for tag in post.tags.all():
            tags.append(tag.name)
    tags = set(tags)
    return {"tags": tags}
