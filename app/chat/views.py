from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required

from chat.models import ChatRoom
from chat.forms import ChatRoomForm

# TODO: move to context processor
CHAT_SERVER_URL = getattr(settings, 'CHAT_SERVER_URL', 'http://localhost')
CHAT_SERVER_PORT = getattr(settings, 'CHAT_SERVER_PORT', '8001')

def chat_login(request, template='chat/signin.html'):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('list-rooms'))

    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))


@login_required
def chat_rooms_list(request, template='chat/rooms.html'):
    existing_rooms = ChatRoom.objects.all()

    if request.method == "POST":
        new_room_form = ChatRoomForm(data=request.POST)
        if new_room_form.is_valid():
            room = new_room_form.save()
            return HttpResponseRedirect(reverse('chat_room', kwargs={'room_name' : room.slug }))
    
    new_room_form = ChatRoomForm()

    context = {
        'existing_rooms' : existing_rooms,
        'new_room_form' : new_room_form,
        'CHAT_SERVER_URL':CHAT_SERVER_URL,
        'CHAT_SERVER_PORT': CHAT_SERVER_PORT,
    }
    return render_to_response(template, context, context_instance=RequestContext(request))


@login_required
def chat_room(request, room_name, template='chat/chat-room.html'):
    context = {
        'CHAT_SERVER_URL': CHAT_SERVER_URL,
        'CHAT_SERVER_PORT': CHAT_SERVER_PORT,
    }
    return render_to_response(template, context, context_instance=RequestContext(request))
