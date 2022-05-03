from django.contrib import admin

# Register your models here.
from net.models import Tipo, Host, Local, Bloco, Snmp


class BlocoInline(admin.TabularInline):
    model = Bloco


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    inlines = [BlocoInline, ]


class SnmpInline(admin.TabularInline):
    model = Snmp

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    inlines = [SnmpInline, ]

@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ['nome','id', 'bloco', 'ipv4', 'net_name', 'tipo']
    list_filter = ['tipo']
