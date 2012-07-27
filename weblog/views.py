from django.http import Http404
from django.template import RequestContext
from weblog.models import Article
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	return render_to_response('index.html', {'article_list': Article.objects.filter(online=True)[:5]}, context_instance=RequestContext(request))

def article(request, n):
	art = get_object_or_404(Article, id=n)
	if  not art.online: raise Http404
	return render_to_response('article.html', {'article': art}, context_instance=RequestContext(request))
