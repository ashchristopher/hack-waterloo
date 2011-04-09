from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext



def chat_rooms_list(request, template='chat/rooms.html'):
	context = {}
	return render_to_response(template, context, context_instance=RequestContext(request))

def chat_room(request, room_name, template='chat/chat-room.html'):
	print room_name

	context = {}
	return render_to_response(template, context, context_instance=RequestContext(request))