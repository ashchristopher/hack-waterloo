from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext

from utils.json_response import JsonResponse

def message_context(request):
    context = {
        'message': {},
        'postrank': {},
    }
    return JsonResponse(context)
