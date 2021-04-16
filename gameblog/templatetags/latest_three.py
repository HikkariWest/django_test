from django import template
from gameblog.models import Post

register = template.Library()


@register.inclusion_tag('gameblog/latest_posts.html')
def latest_three():
    posts = Post.objects.all().filter(publish=True)[:3]
    return {'latest_posts': posts}
