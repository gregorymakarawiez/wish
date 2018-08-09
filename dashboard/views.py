from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {}
    template = loader.get_template('dashboard/index.html')
    return HttpResponse(template.render(context, request))


@login_required
def dashboard(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('dashboard/' + load_template)
    return HttpResponse(template.render(context, request))

