from django.http import HttpResponse
from django.shortcuts import render
from django.db import models


from django.views.generic.base import TemplateView


class JavaView(TemplateView):

    template_name = "java1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        primeiro = self.request.session.get('primeiro', False)

        if not primeiro:
            context['msg'] = 'Bem vindo'
            self.request.session['primeiro'] = True
        else:
            context['msg'] = 'Olá novamente'


        return context
