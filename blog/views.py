from blog.models import BlogEntry
from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    entries = BlogEntry.objects.all()
    template = loader.get_template('blog/index.html')
    context = Context({'entries': entries})
    return HttpResponse(template.render(context))

def details(request, id):
    entry = BlogEntry.objects.get(pk=id)
    template = loader.get_template('blog/details.html')
    context = Context({'entry': entry})
    return HttpResponse(template.render(context))