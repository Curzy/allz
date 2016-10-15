from django.shortcuts import render
from django.views import generic


class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='index.html')
