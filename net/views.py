from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView, ListView

from net.models import Host, Tipo, Snmp
from net.utils.snmp import interfaces, interface


class HostView(DetailView):
    template_name = 'host.html'
    model = Host

    def get_object(self, queryset=None):
        return get_object_or_404(Host, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(HostView, self).get_context_data(**kwargs)
        context['interfaces']=interfaces(context['object'].ipv4,context['object'].snmp_comunidade)
        return context


class InterfaceView(DetailView):
    template_name = 'interface.html'
    model = Host

    def get_object(self, queryset=None):
        return get_object_or_404(Host, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(InterfaceView, self).get_context_data(**kwargs)
        context['interface'] = interface(context['object'].ipv4, context['object'].snmp_comunidade, self.kwargs['interface'])
        return context

class TipoListView(ListView):
    template_name = 'tipolist.html'

    def get_queryset(self):
        return Tipo.objects.order_by('nome')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snmptipo'] = Snmp.objects.order_by('tipo')
        return context


class PingView(ListView):
    template_name = 'ping.html'

    def get_queryset(self):
        return Host.objects.filter(tipo=self.kwargs['pk']).order_by('bloco')


class SnmpView(ListView):
    template_name = 'snmp.html'

    def get_queryset(self):
        #host, comunidade, oid
        #return Snmp.objects.filter(pk=self.kwargs['pk'])
        return Host.objects.values('nome','ipv4', 'tipo', 'tipo__snmp__titulo', 'tipo__snmp__template', 'snmp_comunidade', 'tipo__snmp__oid').filter(tipo__snmp=self.kwargs['pk']).order_by('bloco')