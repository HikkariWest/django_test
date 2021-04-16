from django.shortcuts import render
from .models import Post
from django.db.models import Q


# Create your views here.
def post_details(request, slug):
	post = Post.objects.get(slug = slug)
	context = {'post':post}
	return render(request, 'gameblog/post_details.html', context)


def post_list(request):
	post = Post.objects.all().filter(default = True)
	context = {'post':post}
	return render(request, 'gameblog/post_list.html', context)



'''
search = request.GET.get('search','')
	if search:
		todos = TodoItem.objects.filter(
			Q(title__icontains = search)
				|
			Q(description__icontains = search))
		serialized_todo = serializers.serialize('json', todos, fields = ('title'))
		return JsonResponse({'todos':serialized_todo})
	else:
		todos = TodoItem.objects.all()
	context = {'todos':todos,
				'search':search}
'''
