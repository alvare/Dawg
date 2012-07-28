from datetime import datetime
#from django.utils.timezone import now
#from captchion.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect, Http404, HttpResponse
#from django.core.exceptions import ObjectDoesNotExist

def play(request):
	if request.POST:
		request.session['last_time'] = datetime.now()
		request.session['nick'] = request.POST['nick']
		request.session.save()
		return HttpResponseRedirect('captchion')
	elif request.session.get('nick', False):
		request.session['last_time'] = datetime.now()
		#return render(request, 'captchion/play.html', {'nick': request.session['nick'], 'userlist': [x.get_decoded() for x in Session.objects.all()]})
		return render_to_response('captchion/play.html',{'nick': request.session['nick'], 'userlist': [x.get_decoded() for x in Session.objects.all()]} , context_instance=RequestContext(request))
	else:
		#return render(request, 'captchion/login.html')
		return render_to_response('captchion/login.html', context_instance=RequestContext(request))

def refresh(request):
	if request.POST:
		request.session['last_time'] = datetime.now()
		users = ''
		for ssns in Session.objects.all():
			if (datetime.now() - ssns.get_decoded().get('last_time', False)).seconds > 30:
				ssns.delete()
			else:
				users += '<li>'+ssns.get_decoded().get('nick', None)+'</li>'
		return HttpResponse(users)
	else:
		raise Http404

def reset(request):
	request.session.clear()
	request.session.flush()
	return HttpResponseRedirect('captchion')

def submit(request):
	if request.POST:
		return HttpResponse("caca")
