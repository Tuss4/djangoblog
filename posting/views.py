from django.http import *
from django.shortcuts import *
from posting.models import *
# Create your views here.

def main(request):
	list_of_posts = Post.objects.all()
	return render(request, "post_list.html", {"list": list_of_posts})

def post(request, single):
	single = Post.objects.filter(id=single)
	disqus_code = ['<div id="disqus_thread"></div>','<script type="text/javascript">','var disqus_shortname = "tuss4dzigns";','(function() {','var dsq = document.createElement("script"); dsq.type = "text/javascript"; dsq.async = true;','dsq.src = "//" + disqus_shortname + ".disqus.com/embed.js";','(document.getElementsByTagName("head")[0] || document.getElementsByTagName("body")[0]).appendChild(dsq);','})();','</script>','<noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>',
    	'<a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>']
	if not single:
		raise Http404()
	return render(request, "post.html", {"post": single, "comments": disqus_code})
