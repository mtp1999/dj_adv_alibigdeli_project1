from django.contrib.sitemaps import Sitemap
from appBlog.models import Post
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["appBlog:contact", "appBlog:about"]

    def location(self, item):
        return reverse(item)
