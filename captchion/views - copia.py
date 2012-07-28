from datetime import datetime
from django.utils.timezone import now
from captchion.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.sessions.models import Session
#from django.core.exceptions import ObjectDoesNotExist

def play(request):
	if request.POST:
		request.session['last_time'] = now()
		request.session.save()
		user = User(key=request.session.session_key, online=True, nick=request.POST['nick'])
		user.save()
		return HttpResponseRedirect('captchion')
	elif request.session.get('last_time', False):
		request.session['last_time'] = now()
		return render(request, 'captchion/play.html', {'user': User.objects.get(key=request.session.session_key), 'userlist': User.objects.filter(online=True)})
	else:
		return render(request, 'captchion/login.html')

def refresh(request):
	if request.POST:
		request.session['last_time'] = now()
		User.objects.get(key=request.session.session_key).last_time = now()
		for user in User.objects.all():
			if (now() - user.last_time).total_seconds() > 10:
				user.online = False
				
		return HttpResponse(request.POST['nick'])
	else:
		raise Http404

def reset(request):
	request.session.clear()
	request.session.flush()
	return HttpResponseRedirect('captchion')
