from django.http.response import HttpResponse, Http404
from django.template import loader, Context, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, render, redirect

from organizer.models import Tag, Startup


def redirect_root(request):
    return redirect('organizer_tag_list')

# homepage
def tag_list(request):
    return render(request, "organizer/tag_list.html", {'tag_list': Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, "organizer/tag_detail.html", {'tag': tag})

def startup_list(request):
    return render(request, "organizer/startup_list.html", {'startup_list': Startup.objects.all()})

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, "organizer/startup_detail.html", {'startup': startup})

def tag_form(request):
    return render(request, "organizer/tag_form.html")


