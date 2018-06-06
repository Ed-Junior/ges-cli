from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Person, Documento
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required()
def person_list(request):
    person = Person.objects.all()
    return render(request, 'person.html', {'person': person})

@login_required()
def person_new(request):
    if not request.user.has_perm('clientes.person_add'):
        return HttpResponse("Falha na autenticação")

    form = PersonForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect("person_list")

    return render(request, 'person_form.html', {'form': form})

@login_required()
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()

        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})

@login_required()
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_del.html', {'person': person})


class PersonList(LoginRequiredMixin, ListView):
    model = Person



class PersonDetail(LoginRequiredMixin ,PermissionRequiredMixin, DetailView):
    permission_required = ('permissão2',)

    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PersonCreate(LoginRequiredMixin ,CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'img']
    success_url = '/clientes/list2/'


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'img']
    success_url = reverse_lazy('PersonList')


class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('PersonList')



class BulkView(LoginRequiredMixin, View):
    def get(self, request):
        documentos = ['123456', '147852', '963258', '987456', '91128739']
        lis_doc = []
        for documento in documentos:
            d = Documento(num_doc=documento)
            lis_doc.append(d)

        Documento.objects.bulk_create(lis_doc)
        return HttpResponse('funcionou')





