

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from cadastros.forms import CidadeForm
from cadastros.models import Cidade
from django.core.exceptions import  PermissionDenied

class SidiaBaseListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'PROJETO SIDIA'
        return context

class CidadeList(ListView):

    queryset = Cidade.objects.order_by('nome')
    context_object_name = 'cidades'
    template_name = 'cadastros/lista_cidades.html'

class CidadeDetail(DetailView):

    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    # pk_url_kwarg = 'id'
    template_name = 'cadastros/detalhe_cidades.html'

class CidadeDelete(DeleteView):
    context_object_name = 'cidade'
    # queryset = Cidade.objects.all()
    model = Cidade
    template_name = 'cadastros/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')

class CidadeCreate(CreateView):
    model = Cidade
    # fields = ['nome', 'capital']
    form_class = CidadeForm
    template_name = 'cadastros/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')

class CidadeUpdate(UpdateView, SuccessMessageMixin):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = ' Cadastro Atualizado com Sucesso! '


# class CidadeList(View):
#
#     def get(self, request):
#         qs = Cidade.objects.all().order_by('nome')
#
#         context = {
#             'cidades': qs,
#             'titulo': 'SIDIA'
#         }
#         return render(request, 'cadastros/lista_cidades.html', context)

    # def post(self, request):
    #     pass

# def lista_cidades(request):

    # qs = Cidade.objects.all().order_by('nome')
    #
    # context = {
    #     'cidades': qs,
    #     'titulo': 'SIDIA'
    # }
    # return render(request, 'cadastros/lista_cidades.html', context)

# def detalhe_cidade(request, id):
#
#     # id_cidade = request.objects.GET["id_cidade"]
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     context = {
#         'cidade': cidade
#     }
#
#     return render(request, 'cadastros/detalhe_cidades.html', context)

# @login_required
# def remove_cidade(request, id):
#
#
#
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     cidade.delete()
#
#     return redirect('cidades-list')


# @login_required
# def cadastra_cidade(request):
#
#
#
#     if request.method == 'POST':
#
#             form = CidadeForm(request.POST)
#             if form.is_valid():
#
#                 form.save()
#
#                 return redirect('cidades-list')
#
#     else:
#         form = CidadeForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'cadastros/cadastra_cidades.html', context)
#

# @login_required
# def editar_cidade(request, id):
#
#     # if not request.user.is_authenticated:
#     #     raise PermissionDenied
#
#     # receber dados da cidade e apresentar formulario
#     cidade_obj = get_object_or_404(Cidade, pk=id)
#     form = CidadeForm(request.POST or None, instance=cidade_obj)
#
#     if request.method =='POST':
#         form = CidadeForm(request.POST, instance=cidade_obj)
# # receber dados editados e salvar
#
#         if form.is_valid():
#             form.save()
#             return redirect('cidades-list')
#
#     context = {
#         'form': form,
#         'obj': cidade_obj
#     }
#     return render(request,'cadastros/edita_cidades.html', context)
