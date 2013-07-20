from django.http import *
from django.shortcuts import *
from posting.models import *
from posting.forms import *
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def main(request):
	list_of_posts = Post.objects.all()
	paginator = Paginator(list_of_posts, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, "post_list.html", {"list": posts})

def post(request, single):
	single = Post.objects.filter(id=single)
	comment_form = submit_comment(request.POST)
	post_comments = None 
	if request.method == "POST":
		if comment_form.is_valid():
			clean_data = comment_form.cleaned_data
			new_comment = Comment(
				author=clean_data['name'], 
				date=datetime.datetime.now(), 
				email=clean_data['email'], 
				comment=clean_data['message'], 
				actual_post=single[0])
			new_comment.save()
			HttpResponseRedirect("")
	if Comment.objects.filter(actual_post=single[0]):
		post_comments = Comment.objects.filter(actual_post=single)
	if not single:
		raise Http404()
	return render(request, "post.html", {"post": single, "comment_form": comment_form, "comments": post_comments})

def new_post(request):
	if request.user.is_authenticated():
		create = new_post_form()
		return render(request, "new_post.html", {"form": create})
	raise Http404()

def post_success(request):
	newPost = Post(title=request.POST.get('title'), date=datetime.datetime.now(), author=request.user.username, post=request.POST.get('post') )
	newPost.save()
	return HttpResponseRedirect("/main/")