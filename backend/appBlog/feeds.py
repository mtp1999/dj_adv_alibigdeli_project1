from django.contrib.syndication.views import Feed
from appBlog.models import Post


class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "rss/feed/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:10]
