# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.


def home(request):
    # return render(request, 'home.html')
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('home.html',
                              context_instance=context)
