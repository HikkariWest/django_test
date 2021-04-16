from django import template
from gameblog.models import Post

register = template.Library()

@register.simple.tag
def latest_three():
	posts = Post.objects.filter(publish = True)
	post_last3 = posts[posts.count()-3:]
	return post_last3
