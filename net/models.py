from django.db import models
from net.utils.ping import ping_host


class Tipo(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome


class Local(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome


class Bloco(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return str(self.local)+' - '+str(self.nome)


class Host(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)
    ipv4 = models.GenericIPAddressField(protocol='IPv4', blank=False, null=False)
    net_name = models.CharField('Nome na Rede', max_length=100, blank=True, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, null=False, blank=False)
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT, null=True, blank=True)
    snmp_comunidade = models.CharField('SNMP Comunidade', max_length=100, blank=True, null=True, default='public')

    @property
    def status(self):
        if not self.net_name:
            r = ping_host(self.ipv4)
            if r is not None:
                return str(int(r * 1000))+' ms'
            else:
                return False
        else:
            r = ping_host(self.net_name)
            if r is not None:
                return str(int(r * 1000)) + ' ms ' +(self.net_name)
            else:
                return False

    def __str__(self):
        return self.nome


class Snmp(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, null=False, blank=False)
    titulo = models.CharField('Título', max_length=100, blank=True, null=True)
    oid = models.CharField('Oid', max_length=100, blank=True, null=True)
    template = models.TextField('Template', blank=True, null=True, help_text='Utilize a variavel {{value}} e configure a exibição do valor obtido via SNMP')





