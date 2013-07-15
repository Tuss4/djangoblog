from django.http import *
from django.shortcuts import *
from posting.models import *
# Create your views here.

def main(request):
	list_of_posts = Post.objects.all()
	return render(request, "post_list.html", {"list": list_of_posts})

def post(request, single):
	single = Post.objects.filter(id=single)
	if not single:
		raise Http404()
	return render(request, "post.html", {"post": single})
