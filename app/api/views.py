from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext

from utils.json_response import JsonResponse

def message_context(request):
    print request

    # only posts are valid
    if request.method != 'POST':
        raise Http404

    message = request.POST.get('message', None)
    if not message:
        raise Http404

    # do something with request.POST (pass to pipeline and
    # decorate this context)
    context = {
        'postrank': {
            'rank': 10,
            'url': 'http://blah.com',
        },
    }
    return JsonResponse(context)
