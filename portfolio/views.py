from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.list import ListView
from django.template import loader
from . import models

class MyView(View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template("portfolio.html")
        return HttpResponse(template.render())


class ProjectView(ListView):
    model = models.Project
    template_name = 'portfolio.html'
    context_object_name = 'projects'


    def get_queryset(self):
        return models.Project.objects.all()